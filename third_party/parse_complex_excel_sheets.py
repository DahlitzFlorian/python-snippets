from pathlib import Path

import pandas as pd


path = Path("src/samples.xlsx")
xls = pd.ExcelFile(path)
print(xls.sheet_names)

df = xls.parse(xls.sheet_names[0])
print(df.head())
