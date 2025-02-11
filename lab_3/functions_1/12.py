def space(str):

    cnt = 0

    for x in str:

        if x == " ":

            cnt += 1

    return cnt




a = str(input("Ведите строку: "))

print(space(a))