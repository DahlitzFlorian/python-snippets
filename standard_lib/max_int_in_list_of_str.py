numbers = ["9", "44", "8", "222"]

max_string = max(numbers)
print(f"Max string: {max_string}")

max_number = max(numbers, key=int)
print(f"Max number: {max_number}")
