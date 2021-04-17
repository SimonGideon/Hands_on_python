# Issues_and_limitations
print(1 / 10)
import math

print(format(math.pi, '.12g'))  # give 12 significant digits

print(format(math.pi, '.2f'))  # give 2 digits after the point

print(repr(math.pi))
print(.1 + .1 + .1 == .3)
print(round(.1 + .1) + round(.1, 1) + round(.1, 1) == round(.3, 1))
print(round(.1 + .1 + .1, 10) == round(.3, 10))

x = 3.14159
x.as_integer_ratio()
print(x == 3537115888337719 / 11258999068426224)
print(x.hex())  # expresses a float in hexadecimal (base 16)
print(sum([0.1] * 10) == 1.0)
print(math.fsum([0.1] * 10) == 1.0)


