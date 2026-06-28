arr = [2, 4, 3, 5, 7, 8]
target = 10

seen = set()

for num in arr:
    complement = target - num

    if complement in seen:
        print(complement, num)

    seen.add(num)