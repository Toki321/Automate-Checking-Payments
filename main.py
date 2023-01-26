import os

from getArrThatContains314or318 import getArrThatContains314or318
from getArrThatDoesntContainNeededWords import doesntContainWordsArr


contains314Arr = getArrThatContains314or318(314)

contains318Arr = getArrThatContains314or318(318)


pdfFolder = './DDT'

fileNamesList = os.listdir('./DDT')

searchWords314 = ['tel.', 'preavviso', 'Preavviso', "Tel."]
searchWords318 = ['idraulica', 'Idraulica']

# For 314
doesnNotContainArr314 = doesntContainWordsArr(
    contains314Arr, searchWords314, pdfFolder, fileNamesList)

# For 318
# doesnNotContainArr318 = doesntContainWordsArr(
#     contains318Arr, searchWords318, pdfFolder, fileNamesList)

with open("314December2021NotContainedFixed", "w") as f:
    for string in doesnNotContainArr314:
        f.write(string + '\n')
