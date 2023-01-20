import pandas as pd
import os
import PyPDF2

from helpers import isMatch
from test import december_314

# Read an Excel file
df = pd.read_excel('excelFile.xlsx', sheet_name='Dicembre 2021')

# Fill the missing values in the first column with the previous non-null value
df.iloc[:, 0].fillna(method='ffill', inplace=True)

# Create a boolean mask to filter the rows where the second column is 314
mask_314 = (df.iloc[:, 1] == 314)

# Use boolean mask to filter the rows
filtered_df_314 = df[mask_314]
result_array_314 = filtered_df_314.iloc[:, 0].tolist()
result_array_314 = list(set(result_array_314))

# Create a boolean mask to filter the rows where the second column is 318
mask_318 = (df.iloc[:, 1] == 318)

# Use boolean mask to filter the rows
filtered_df_318 = df[mask_318]
result_array_318 = filtered_df_318.iloc[:, 0].tolist()
result_array_318 = list(set(result_array_318))

result_array_314 = [str(x) for x in filtered_df_314.iloc[:, 0].tolist()]
result_array_314 = list(set(result_array_314))

result_array_318 = [str(x) for x in filtered_df_318.iloc[:, 0].tolist()]
result_array_318 = list(set(result_array_318))

new_result_array_314 = []
new_result_array_318 = []


dividedByDash314 = []

for x in result_array_314:
    if '-' in x:
        split_string = x.split('-')
        for string in split_string:
            dividedByDash314.append(string)


result_array_314.extend(dividedByDash314)

unique_array_314 = list(set(result_array_314))


dividedByDash318 = []

for x in result_array_318:
    if '-' in x:
        split_string = x.split('-')
        for string in split_string:
            dividedByDash318.append(string)


result_array_318.extend(dividedByDash318)

unique_array_318 = list(set(result_array_318))


pdf_folder = './DDT'

fileList = os.listdir('./DDT')

# words to search for in the pdfs
search_word_314 = 'tel.'
search_word_318 = 'idraulica'

doesNOTContain314 = []

for word in unique_array_314:
    for file in fileList:
        if isMatch(word, file):
            pdf_path = os.path.join(pdf_folder, file)
            reader = PyPDF2.PdfReader(pdf_path)
            for page in reader.pages:
                pdf_text = page.extract_text()
                if (search_word_314 in pdf_text) == False:
                    print(f'{file} doesnt contains the word {search_word_314}')
                    doesNOTContain314.append(file)
                    break


doesNOTContain318 = []

for word in unique_array_318:
    for file in fileList:
        if isMatch(word, file):
            pdf_path = os.path.join(pdf_folder, file)
            reader = PyPDF2.PdfReader(pdf_path)
            for page in reader.pages:
                pdf_text = page.extract_text()
                if (search_word_318 in pdf_text) == False:
                    print(f'{file} doesnt contains the word {search_word_318}')
                    doesNOTContain318.append(file)
                    break
