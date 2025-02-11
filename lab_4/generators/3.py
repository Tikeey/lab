def iterate_numbers(N):

    for i in range(0, N + 1):

        if(i % 3 == 0 and i % 4 == 0):

            yield i  

N = int(input("Enter a number N: "))

for square in iterate_numbers(N):
    
    print(square)
