import os

from getArrThatContains314or318 import getArrThatContains314or318
from getArrThatDoesntContainNeededWords import doesntContainWordsArr
from helpers import extractNumber, remove_after_dash, remove_last_letter


contains314Arr = getArrThatContains314or318(314)

contains318Arr = getArrThatContains314or318(318)


pdfFolder = './DDT'

fileNamesList = os.listdir('./DDT')

file_names_dict = {}

for fileName in fileNamesList:
    try:
        number = extractNumber(fileName)
        number = remove_last_letter(number)
        key = int(number)
    except:
        key = int(remove_after_dash(
            remove_last_letter(extractNumber(fileName))))

    file_names_dict[key] = fileName


searchWords314 = ['tel.', 'preavviso', 'Preavviso', "Tel."]
searchWords318 = ['idraulica', 'Idraulica']

###
# For 314
doesnNotContainArr314 = doesntContainWordsArr(
    contains314Arr, searchWords314, pdfFolder, file_names_dict)

doesnNotContainArr314 = list(set(doesnNotContainArr314))

with open("314Giugno 2022.txt", "w") as f:
    for string in doesnNotContainArr314:
        f.write(string + '\n')
###


# For 318
doesnNotContainArr318 = doesntContainWordsArr(
    contains318Arr, searchWords318, pdfFolder, file_names_dict)

doesnNotContainArr318 = list(set(doesnNotContainArr318))

with open("318Giugno 2022.txt", "w") as f:
    for string in doesnNotContainArr318:
        f.write(string + '\n')
###
