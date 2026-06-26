def perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num


n = int(input("Enter a number: "))

if perfect(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")