data = [1, 2, 3, 4, 5, 6, 7]
low, high = 3, 6
result = sum(low <= x < high for x in data)

print(result)
