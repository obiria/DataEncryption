def pow_h(base, exponent, modulus):
        """Fast modular exponentiation"""
        result = 1
        if 1 & exponent:
            result = base
        while exponent:
            exponent >>= 1
            base= (base * base) % modulus
            if exponent & 1:result = (result * base) % modulus
        return result