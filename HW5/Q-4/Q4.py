def number_triangle(n):
    count = 1
    i = 1
    while i <= n:
        for j in range(1, i+1):
            print(count, end = ' ')
            count +=1
        i +=1
        print("\n")
number_triangle(6)