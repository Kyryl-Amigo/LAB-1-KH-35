N = int(input("Введіть ціле число N (1 < N < 9): "))

if 1 < N < 9:
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            print(j, end=" ")
        print()
else:
    print("Введіть число в діапазоні від 2 до 8.")
