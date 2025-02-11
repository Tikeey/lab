import math

def polygon_area(n, l):

    return round((n * l**2) / (4 * math.tan(math.pi / n)), 3)

n = int(input("Input number of sides: "))

l = float(input("Input the length of a side: "))

print("The area of the polygon is: ", polygon_area(n, l))

