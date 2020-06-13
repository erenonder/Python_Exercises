

class Polynomial:

    def __init__(self, *coefs):
        self.coefs = coefs

    def __repr__(self):
        return "This is polynomial with coefficients {}".format(self.coefs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coefs, other.coefs)))


pol1 = Polynomial(1, 2, 3)
pol2 = Polynomial(3, 4, 5)


# mytup1 = (0, 1)
# mytup2 = (2, 3)

# mygen = (x + y for x, y in zip(mytup1, mytup2))
# print(*mygen)

print(pol1 + pol2)
