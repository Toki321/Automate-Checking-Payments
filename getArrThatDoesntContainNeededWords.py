import PyPDF2
import os

from helpers import isMatch, isSearchWordsContainedInText


def doesntContainWordsArr(contains314or318Arr, searchWordsArr, pdfFolder, fileNamesDict):
    doesNOTContain = []

    for strNumber in contains314or318Arr:
        try:
            print(strNumber)
            fileName = fileNamesDict[int(strNumber)]
            print(fileName)
            pdf_path = os.path.join(pdfFolder, fileName)
            reader = PyPDF2.PdfReader(pdf_path)
            for page in reader.pages:
                pdf_text = page.extract_text()
                if isSearchWordsContainedInText(searchWordsArr, pdf_text) == False:
                    doesNOTContain.append(fileName)
        except:
            print(strNumber, "doesnt exist")
    return doesNOTContain


# pdf_path = os.path.join(
#     "./DDT", "DDT-3898_2021-IMPRESA-UNO-Snc-di-Conti-Giorgio--C.pdf")


# reader = PyPDF2.PdfReader(pdf_path)
# for page in reader.pages:
#     pdf_text = page.extract_text()
#     if isSearchWordsContainedInText(["tel"], pdf_text):
#         print('contained')
