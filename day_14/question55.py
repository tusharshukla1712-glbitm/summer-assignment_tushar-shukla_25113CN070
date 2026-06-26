arr = list(map(int, input("Enter array elements: ").split()))

largest = second = float("-inf")

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest element =", second)