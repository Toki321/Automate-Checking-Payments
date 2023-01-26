import numpy as np
import pandas as pd
import os


from getArrThatContains314or318 import getArrThatContains314or318


contains314Arr = getArrThatContains314or318(314)

contains318Arr = getArrThatContains314or318(318)


pdf_folder = './DDT'

fileList = os.listdir('./DDT')

searchWords314 = ['tel.', 'preavviso']
searchWord318 = ['idraulica']

# pdf_folder = './DDT'

# fileList = os.listdir('./DDT')

# # words to search for in the pdfs
# search_word_314 = 'tel.'
# search_word_314_2 = 'preavviso'
# search_word_318 = 'idraulica'

# doesNOTContain314 = []

# for word in final_array_314:
#     for file in fileList:
#         if isMatch(word, file):
#             pdf_path = os.path.join(pdf_folder, file)
#             reader = PyPDF2.PdfReader(pdf_path)
#             for page in reader.pages:
#                 pdf_text = page.extract_text()
#                 if (search_word_314 in pdf_text) == False:
#                     print(f'{file} doesnt contains the word {search_word_314}')
#                     doesNOTContain314.append(file)
#                     break


# doesNOTContain318 = []

# for word in final_array_318:
#     for file in fileList:
#         if isMatch(word, file):
#             pdf_path = os.path.join(pdf_folder, file)
#             reader = PyPDF2.PdfReader(pdf_path)
#             for page in reader.pages:
#                 pdf_text = page.extract_text()
#                 if (search_word_318 in pdf_text) == False:
#                     print(f'{file} doesnt contains the word {search_word_318}')
#                     doesNOTContain318.append(file)
#                     break

# f314 = open("314december2021.txt", "w")
# for file in doesNOTContain314:
#     f314.write(file + "\n")

# f318 = ("318december2021.txt", "w")
# for file in doesNOTContain318:
#     f314.write(file + "\n")
