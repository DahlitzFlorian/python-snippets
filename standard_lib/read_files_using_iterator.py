"""
Reveals the usage of iterators to read in a file. It's useful when dealing with large files.
If not using iterators, the whole file is loaded into memory at one (think of several gigabyte
huge files). If using iterators, only the next line is loaded.
"""
print(next(open("huge_log_file.txt")))
