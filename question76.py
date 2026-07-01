n = int(input("Enter size of square matrix: "))

matrix = []

print("Enter the matrix:")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

sum = 0

for i in range(n):
    sum = sum + matrix[i][i]

print("Diagonal Sum =", sum)