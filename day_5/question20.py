num = int(input("Enter a number: "))

largest = 1
n = num

factor = 2

while factor <= n:
    if n % factor == 0:
        largest = factor
        n //= factor
    else:
        factor += 1

print("Largest Prime Factor =", largest)
