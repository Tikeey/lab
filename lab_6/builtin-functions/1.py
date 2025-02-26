list = []

a = int(input("Введите количество элементов: "))

for x in range(a):

    b = int(input("Введите элемент: "))

    list.append(b)

res = eval('*'.join(map(str, list)))

print("Product of all elements: ", res)
