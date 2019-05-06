import fnmatch
import os
import re


reg = "({})|({})".format(fnmatch.translate("*.md"), fnmatch.translate("*.git*"))
markdown_files = [f for f in os.listdir() if re.match(reg, f)]

print(markdown_files)
