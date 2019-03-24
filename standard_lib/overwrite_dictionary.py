defaults = {"lenny": "white", "carl": "black"}
overwrite = {"lenny": "yellow"}
new = {**defaults, **overwrite}

print(new)
