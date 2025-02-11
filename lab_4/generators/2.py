def even_numbers(N):

    for i in range(0, N + 1):

        if(i % 2 == 0):

            yield i  

N = int(input("Enter a number N: "))

for square in even_numbers(N):
    
    print(square)
