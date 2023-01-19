import pandas as pd

# Read all sheets in the Excel file
df = pd.read_excel('excelFile.xlsx', sheet_name=None)

# Print the names of all sheets
print(df.keys())

# Iterate over the sheets and print the first 5 rows of each sheet
for sheet_name, data in df.items():
    print(sheet_name)
    print(data.head())
