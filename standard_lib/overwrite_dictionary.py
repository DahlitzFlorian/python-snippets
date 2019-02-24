"""
Loving Python3.5 PEP 448 for overwriting a dictionary 
of default values
"""
defaults = {"lenny": "white", "carl": "black"}
overwrite = {"lenny": "yellow"}
new = {**defaults, **overwrite}

print(new)
