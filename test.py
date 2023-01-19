import pandas as pd

# Read an Excel file
df = pd.read_excel('excelFile.xlsx')

# Create an empty array to store the data from the first column
result_array = []

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Check if the value in the second column is 314 or 318
    if row['B'] == 314 or row['B'] == 318:
        # Append the data from the first column to the result array
        result_array.append(row['A'])
