from distutils import filelist
import PyPDF2
import os

from helpers import isMatch, isSearchWordsContainedInText


def doesntContainWordsArr(contains314or318Arr, searchWordsArr, pdfFolder, fileNamesList):
    doesNOTContain = []

    print("what")

    for strNumber in contains314or318Arr:
        print("entered first loop")
        for fileName in fileNamesList:
            print("entered second loop")
            if isMatch(strNumber, fileName):

                pdf_path = os.path.join(pdfFolder, fileName)
                reader = PyPDF2.PdfReader(pdf_path)
                for page in reader.pages:
                    pdf_text = page.extract_text()
                    if isSearchWordsContainedInText(searchWordsArr, pdf_text) == False:
                        doesNOTContain.append(fileName)
                break

    return doesNOTContain
