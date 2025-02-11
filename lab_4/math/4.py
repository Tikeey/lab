import math

def parallelogram_area(a, h):

    return round(math.prod([a, h]), 1)


a = float(input("Length of base: "))

h = float(input("Heightof parallelogram: "))

print("Expected Output: ", parallelogram_area(a, h))