from core.prime_numbers import primeNumber
from core.Karatsuba import  karatsuba
from core.Pow_h import pow_h
from core.Inverse import Inv 

"""
Implementation of  RSA: November 24, 2020
"""
debug = False
class rsa(object):
    def __init__(self, bit_length=100):
        self.prime = primeNumber(bit_length)
   
    def keyGen(self):
        """Key Generation
         I. Choose two distinct prime numbers p and q.
         II. Find n such that n = pq.
         n will be used as the modulus for both the public and private keys.
         III. Find the totient of n, phi(n) such that phi(n)=(p-1)(q-1).
         IV. Choose an e such that 1 < e < phi(n), and such that e and phi(n) share no divisors other than 1 (e and phi(n) are relatively prime).
         e is kept as the public key exponent
         V. Determine d (using modular arithmetic) which satisfies the congruence relation de ≡ 1 (mod phi(n)).
        """
        p = self.prime.generate_primes()[0]
        q = self.prime.generate_primes()[0]
        n = karatsuba(p,q)
        phi_n = karatsuba((p-1),(q-1))
    
        e = self.prime.generate_primes()[0]
        gcd,_,_ = Inv.egcd_binary(e,phi_n)
        
         
        if 1 < e < phi_n and gcd == 1:
            d = Inv().inverse(e,phi_n)
            public_key ={'n':n,'e':e}
            sk = {'sk':d}
            if d*e%phi_n !=1:
                raise AssertionError ("The value of d is invalid") 
        else:
            raise AssertionError ("The value of e is invalid")
        
        return  public_key,sk 
   
    def Encryption(self,pk, m):
        """
         2. Encryption
         I. Person A transmits his/her public key (modulus n and exponent e) to Person B, keeping his/her private key secret.
         II. When Person B wishes to send the message "M" to Person A, he first converts M to an integer such that 0 < m < n by
         using agreed upon reversible protocol known as a padding scheme.
         III. Person B computes, with Person A's public key information, the ciphertext c corresponding to
         c ≡ m^e(mod n).
         IV. Person B now sends message "M" in ciphertext, or c, to Person A.
        """
        if 0 < m < pk['n']:

            c = pow_h(m,pk['e'],pk['n'])
            Ct = {'Ct':c, 'n':pk['n']}
        else:
            raise AssertionError ("The value of m is invalid")
        
        return Ct


    def Decryption(self, Ct,sk):
        """3. Decryption
        I. Person A recovers C from B by using his/her private key exponent, d the is recovered by reversing the padding scheme:
        by the computation m ≡ c^d (mod n)"""
        d = sk['sk']
        C = Ct['Ct']
        n=  Ct['n']
        m = pow_h(C,d, n)
        message = {'message':m}
        return message 


if __name__ == '__main__':
    # Since it is pure python implementation the size of bit_length of 1024 bit takes time
    bit_length = 100

    prime = primeNumber(bit_length)
    m = prime.generate_primes()[0] #message m
    
    y = rsa(bit_length)
    pk,sk = y.keyGen()
    if debug:print(pk,sk)

    Ct = y.Encryption(pk,m)
    
    if debug:print(Ct)
    
    msg = y.Decryption(Ct, sk)
    
    
    if m ==msg['message']:
        print('Successful mesaage recovery')
    else:
        raise AssertionError ("Fail decryption of the message")



        



