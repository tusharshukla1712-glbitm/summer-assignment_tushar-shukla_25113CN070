n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even elements =", even)
print("Odd elements =", odd)