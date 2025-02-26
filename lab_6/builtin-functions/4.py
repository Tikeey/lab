import time
import math

num = int(input("Введите число: "))

delay = int(input("Введите задержку: "))

time.sleep(delay / 1000) 

res = math.sqrt(num)

print(f"Square root of {num} after {delay} milliseconds is {res}")
