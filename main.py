import pandas as pd
import os
import PyPDF2

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

# Remove duplicates from the result array
result_array_final = list(set(result_array))

pdf_folder = 'path/to/pdfs'

# words to search for in the pdfs
search_words = ['idraulica', 'preavviso']

for pdf_name in result_array_final:
    pdf_path = os.path.join(pdf_folder, f"{pdf_name}.pdf")
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_file.close()
    for page in range(pdf_reader.getNumPages()):
        pdf_text = pdf_reader.getPage(page).extractText()
        for word in search_words:
            if word in pdf_text:
                print(f'{pdf_name}.pdf contains the word {word}')
                break
