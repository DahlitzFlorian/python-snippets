import json


nums = [1, 2, 3]
chars = ["a", "b", "c"]

alph = dict(zip(nums, chars))
print(json.dumps(alph, indent=4, sort_keys=True))
