from collections import OrderedDict


a = ["foo", "Alice", "bar", "foo", "Bob"]
print(f"List with duplicates: {a}")

a = list(OrderedDict.fromkeys(a).keys())
print(f"Without duplicates: {a}")
