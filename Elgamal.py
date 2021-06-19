from core.prime_numbers import primeNumber
from core.Pow_h import pow_h
from core.Inverse import Inv 

debug = False

"""
Implementation of  ELgamal encryption scheme: November 24, 2020
"""
class elgamal(object):
    def __init__(self, bit_length= 100):
        self.prime = primeNumber(bit_length)

    def keyGen(self):
        """
         1) Key generation 
         Suppose Alice wants to communicate to Bob.
         Bob generates public and private key :
         1. Bob chooses a very large number q and a cyclic group Fq.
         2. From the cyclic group Fq, he choose any element g and an element a such that gcd(a, q) = 1.
         3. Then he computes h = g^a.
         4. Bob publishes F, h = g^a, q and g as his public key and retains a as private key.
        """
        q = self.prime.generate_primes()[0]
        g = self.prime.generate_primes()[0]
        a = self.prime.generate_primes()[0]
    
        gcd,_,_ = Inv.egcd_binary(a,q)
        
         
        if gcd == 1:
            h = pow_h(g,a, q)
            public_key ={'h':h, 'g':g, 'q':q}
            sk = {'sk':a}
        else:
            raise AssertionError ("The value of a is invalid")
        
        return  public_key,sk 
    
    def Encryption(self,pk, m):
        """
        2. Encryption
        Alice encrypts data using Bob’s public key :
        Alice selects an element k from cyclic group F
        such that gcd(k, q) = 1.
        Then she computes p = gk and s = hk = gak.
        She multiples s with M.
        Then she sends (p, M*s) = (gk, M*s)."""
        g = pk['g']
        q = pk['q']
        h = pk['h']
        k = self.prime.generate_primes()[0]
        gcd,_,_ = Inv.egcd_binary(k,q)
         
        if gcd == 1:
            s = pow_h(h,k, q)
            p = pow_h(g,k, q)
            C = m^s 
            public_key ={'p':p, 'C':C, 'q':q,'s':s}
            sk = {'sk':k}
        else:
            raise AssertionError ("The value of a is invalid")
        
        
        return public_key,sk 
   
    def Decryption(self, Ct,sk):
        """3. Decryption
        Bob decrypts the message : Bob calculates s′ = pa = gak.
        He xor M^s' to obtain M as s = s'.
       """
        a = sk['sk']
        C = Ct['C']
        p = Ct['p']
        q = Ct['q']
        s = pow_h(p,a, q)
    
        m  = C^s
        message = {'message':m}
        return message 


if __name__ == '__main__':
    # Since it is pure python implementation the size of bit_length of 1024 bit takes time
    bit_length = 100

    prime = primeNumber(bit_length)
    m = prime.generate_primes()[0] #message m
    
    y = elgamal(bit_length)
    pk,sk = y.keyGen()
    if debug:print(pk,sk)

    Ct,sk_ = y.Encryption(pk,m)
    if debug:print(Ct)
    
    msg = y.Decryption(Ct, sk)
    
    
    if m ==msg['message']:
        print('Successful mesaage recovery')
    else:
        raise AssertionError ("Fail decryption of the message")



        



