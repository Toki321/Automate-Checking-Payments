import pandas as pd
import os
import PyPDF2

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

for i in range(len(result_array_314)):
    if '-' in result_array_314[i]:
        split_string = result_array_314[i].split('-')
        for string in split_string:
            new_result_array_318.append(string)
    else:
        new_result_array_314.append(result_array_314[i])

for i in range(len(result_array_318)):
    if '-' in result_array_318[i]:
        split_string = result_array_318[i].split('-')
        for string in split_string:
            new_result_array_318.append(string)
    else:
        new_result_array_318.append(result_array_318[i])

print(new_result_array_314)
print(new_result_array_318)

pdf_folder = './'

# words to search for in the pdfs
search_word_314 = 'tel'
search_word_318 = 'idraulica'

# search for 314 array pdfs
# for pdf_name in new_result_array_314:
#     pdf_path = os.path.join(pdf_folder, f"{pdf_name}.pdf")
#     pdf_file = open(pdf_path, 'rb')
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#     pdf_file.close()
#     for page in range(pdf_reader.getNumPages()):
#         pdf_text = pdf_reader.getPage(page).extractText()
#         if search_word_314 in pdf_text:
#             print(f'{pdf_name}.pdf contains the word {
