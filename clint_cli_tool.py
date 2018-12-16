import os
import sys

from clint.arguments import Args
from clint.textui import puts, colored, indent

sys.path.insert(0, os.path.abspath(".."))

args = Args()

with indent(4, quote=">>>"):
    puts(colored.blue("Arguments passed in: ") + str(args.all))
    puts(colored.blue("Flags detected: ") + str(args.flags))
    puts(colored.blue("Files detected: ") + str(args.files))
    puts(colored.blue("NOT Files detected: ") + str(args.not_files))
    puts(colored.blue("Grouped Arguments: ") + str(dict(args.grouped)))

print()
