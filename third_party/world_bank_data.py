import csv
import io
import zipfile

import requests


url = "http://databank.worldbank.org/data/download/WDI_csv.zip"
filename = "WDIData.csv"

# Warning: this can take two minutes to download!!
with zipfile.ZipFile(io.BytesIO(requests.get(url).content)) as zip_file:
    print("\n".join(name for name in zip_file.namelist()))
    zip_file.extractall()

# On Python 2, remove: ", newline=''"
with open(filename, newline="") as in_file:
    for row in csv.reader(in_file):
        print(", ".join(row))
