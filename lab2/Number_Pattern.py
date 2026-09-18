n = int(input("Enter n: "))

for i in range(1, 2 * n):
    for j in range(1, 2 * n):

        if i <= n:
            x = i
        else:
            x = 2 * n - i

        if j <= n:
            y = j
        else:
            y = 2 * n - j

        if x <= y:
            print(n - x + 1, end=" ")
        else:
            print(n - y + 1, end=" ")

    print()