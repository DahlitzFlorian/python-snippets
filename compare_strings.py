from difflib import SequenceMatcher


s1 = "This is my string"
s2 = "This is my new string"

s = SequenceMatcher(None, s1, s2)

print(round(s.ratio(), 3))

for block in s.get_matching_blocks():
    a, b, size = block
    print(f"a[{a}] and b[{b}] match for {size} elements")
