
n = int(input("Introduce un número entero positivo: "))

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(2 * j - 1, end=" ")
    print()
