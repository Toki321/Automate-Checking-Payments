import pandas as pd

# Read an Excel file
df = pd.read_excel('excelFile.xlsx', sheet_name='Dicembre 2021')

# Fill the missing values in the first column with the previous non-null value
df.iloc[:, 0].fillna(method='ffill', inplace=True)

# Create a boolean mask to filter the rows where the second column is 314 or 318
mask = (df.iloc[:, 1] == 314) | (df.iloc[:, 1] == 318)

# Use boolean mask to filter the rows
filtered_df = df[mask]

# Extract the values from the first column
result_array = filtered_df.iloc[:, 0].tolist()


result_array_final = list(set(result_array))
print(result_array_final)
