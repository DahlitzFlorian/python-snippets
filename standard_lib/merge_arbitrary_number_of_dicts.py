dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4, 3: 9}
dict3 = {"a": 2}
dict4 = {"d": 8, "e": 1}

print("Result of merging dict 1-4:", {**dict1, **dict2, **dict3, **dict4})
