arr = [1, 2, 3, 2, 4, 2, 5, 3]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_element = max(frequency, key=frequency.get)

print("Element:", max_element)
print("Frequency:", frequency[max_element])