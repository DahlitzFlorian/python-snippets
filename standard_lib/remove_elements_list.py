data = [1, 2, 3, 4, 1, 2, 3, 4]
target = 1

print(f"Original: {data}")

data[:] = [elem for elem in data if elem != target]

print(f"New: {data}")
