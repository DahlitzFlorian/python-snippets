import shlex


sample = 'This is "Berlin Cafe"'
split_str = sample.split()
shlex_str = shlex.split(sample)
some = shlex.quote(sample)

print(f"Split string output: {split_str}")
print(f"Shlex string outpur: {shlex_str}")
