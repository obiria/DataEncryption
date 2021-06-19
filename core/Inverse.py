class Inv(object):
    def __init__(self):
        pass

    @staticmethod
    def egcd_binary(a, b= None):# b is the mode
        u, v, s, t, r = 1, 0, 0, 1, 0
        while (a % 2 == 0) and (b % 2 == 0):
            a, b, r = a//2, b//2, r+1
        alpha, beta = a, b
        while (a % 2 == 0):
            a = a//2
            if (u % 2 == 0) and (v % 2 == 0):
                u, v = u//2, v//2
            else:
                u, v = (u + beta)//2, (v - alpha)//2
        while a != b:
            if (b % 2 == 0):
                b = b//2
                if (s % 2 == 0) and (t % 2 == 0):
                    s, t = s//2, t//2
                else:
                    s, t = (s + beta)//2, (t - alpha)//2
            elif b < a:
                a, b, u, v, s, t = b, a, s, t, u, v
            else:
                b, s, t = b - a, s - u, t - v
        return (2 ** r) * a, s, t


    def inverse(self, a,b):
        _, b, _ = self.egcd_binary(a,b)
        return b

if __name__ == '__main__':
    y = Inv
    z = y.inverse(4,17)
    g= y.egcd_binary(4,17)
    b = "{},{},".format(g,z)
    print(b)
