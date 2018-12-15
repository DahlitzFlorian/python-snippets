"""Reference: https://medium.com/@chrisdoucette15/printing-in-color-with-python-816e6f318dfd"""
from termcolor import colored, cprint

# Normal print
print("Hello World!")

# Normal print with colored text
text = colored("Hello Red World!", "red")
print(text)

# Termcolor colored print
cprint("Hello Blue World!", "blue")
