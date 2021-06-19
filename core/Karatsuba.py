def karatsuba(x,y):
        """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
        if (len(str(x)) == 1 or len(str(y)) == 1):
            return x*y
        else:
            m = max(len(str(x)),len(str(y)))
            m2 = m // 2
            a = x // 10**(m2)
            b = x % 10**(m2)
            c = y // 10**(m2)
            d = y % 10**(m2)
            z0 = karatsuba(b,d)
            z1 = karatsuba((a+b),(c+d))
            z2 = karatsuba(a,c)
        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)