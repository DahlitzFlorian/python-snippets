"""Reference: https://medium.com/ediblesec/building-a-hashing-tool-with-python-3afe34db74e5"""
import os
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

md5 = hashlib.md5()
sha1 = hashlib.sha1()

try:
    with open(args.file, "rb") as f:
        buf = f.read()
        md5.update(buf)
        sha1.update(buf)

    print(f"Filename: {os.path.basename(args.file)}")
    print(f"MD5-Hash: {md5.hexdigest()}")
    print(f"SHA1-Hash: {sha1.hexdigest()}")
except FileNotFoundError as e:
    print(e)
