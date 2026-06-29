arr1 = list(map(int, input("Enter first array elements: ").split()))
arr2 = list(map(int, input("Enter second array elements: ").split()))

union = list(set(arr1) | set(arr2))

print("Union:", union)