from distutils import filelist
import PyPDF2
import os


def doesntContainWordsArr(contains314or318Arr, neededWordsArr, pdfFolder, fileList):
    doesNOTContain314 = []

    for word in final_array_314:
        for file in filelist:
            if isMatch(word, file):
                pdf_path = os.path.join(pdfFolder, file)
                reader = PyPDF2.PdfReader(pdf_path)
                for page in reader.pages:
                    pdf_text = page.extract_text()
                    if (search_word_314 in pdf_text) == False:
                        print(
                            f'{file} doesnt contains the word {search_word_314}')
                        doesNOTContain314.append(file)
                        break
