import math

def convert(num):

    b = math.radians(num)

    return round(b, 6)

a = float(input("Input degree: "))

print("Output radian: ", convert(a))