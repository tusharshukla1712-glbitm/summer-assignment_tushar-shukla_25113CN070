n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    # Ascending characters
    for j in range(i):
        print(chr(65 + j), end="")

    # Descending characters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()