start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong Numbers:")

for num in range(start, end + 1):
    digits = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num, end=" ")
