def palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    if temp == rev:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")