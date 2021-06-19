#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import time
# import re
import random
import math

class primeNumber(object):

    def __init__(self, n):
        self.n  =  n

    
    @staticmethod
    def fermat_primality_test(p, s=5):
        """
        a^(p-1) ≡ 1 mod p
        Input: prime candidate p and security paramter s
        Output: either p is a composite (always trues), or
                p is a prime (with probability)
        """
        if p == 2:
            return True
        if not p & 1: # if p is even, number cant be a prime
            return False

        for i in range(s):
            a = random.randrange(2, p-2)
            x = pow(a, p-1, p) # a**(p-1) % p
            if x != 1:
                return False
        return True

    @staticmethod
    def square_and_multiply(x, k, p=None):
        """
        Square and Multiply Algorithm
        Parameters: positive integer x and integer exponent k,
                    optional modulus p
        Returns: x**k or x**k mod p when p is given
        """
        b = bin(k).lstrip('0b')
        r = 1
        for i in b:
            r = r**2
            if i == '1':
                r = r * x
            if p:
                r %= p
        return r

    @classmethod
    def miller_rabin_primality_test(cls, p, s=5):
        if p == 2: # 2 is the only prime that is even
            return True
        if not (p & 1): # n is a even number and can't be prime
            return False

        p1 = p - 1
        u = 0
        r = p1  # p-1 = 2**u * r

        while r % 2 == 0:
            r >>= 1
            u += 1

        # at this stage p-1 = 2**u * r  holds
        assert p-1 == 2**u * r

        def witness(a):
            """
            Returns: True, if there is a witness that p is not prime.
                    False, when p might be prime
            """
            z = cls.square_and_multiply(a, r, p)
            if z == 1:
                return False

            for i in range(u):
                z = cls.square_and_multiply(a, 2**i * r, p)
                if z == p1:
                    return False
            return True

        for j in range(s):
            a = random.randrange(2, p-2)
            if witness(a):
                return False

        return True
    
    def generate_primes(self):
        k=1
        """
        Generates prime numbers with bitlength n.
        Stops after the generation of k prime numbers.

        Caution: The numbers tested for primality start at
        a random place, but the tests are drawn with the integers
        following from the random start.
        """
        assert k > 0
        assert self.n > 0 and self.n < 4096

        # follows from the prime number theorem
        '''necessary_steps = math.floor( math.log(2**n) / 2 )'''
        # get n random bits as our first number to test for primality
        x = random.getrandbits(self.n)
    

        primes = []

        while k>0:
            if  primeNumber.miller_rabin_primality_test(x, s=7):
                primes.append(x)
                k = k-1
            x = x+1

        return primes
    
    def main(self):
        #cls.n = 2048
        primes = primeNumber.generate_primes(self.n)
        for p in primes:
            print('{} {}'.format(p, self.n))

if __name__ == '__main__':
    y = primeNumber(1024)
    z = y.generate_primes()
    b = "{},".format(z)
    print(b)

