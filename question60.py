arr = [1, 0, 2, 0, 3, 0, 4]

result = []

for i in arr:
    if i != 0:
        result.append(i)

while len(result) < len(arr):
    result.append(0)

print(result)