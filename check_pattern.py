"""
Check for multiple string patterns.
"""
lst = ["hello", "fafaea", "hello world", "xxx world", "zzz"]
patterns = ["hello", "world"]

result = [item for item in lst if any(pattern in item for pattern in patterns)]

print(result)
