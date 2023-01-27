import os
from threading import Thread

from getArrThatContains314or318 import getArrThatContains314or318
from getArrThatDoesntContainNeededWords import doesntContainWordsArr
from helpers import extractNumber, remove_after_dash, remove_last_letter


contains314Arr = getArrThatContains314or318(314)

contains318Arr = getArrThatContains314or318(318)


pdfFolder = './DDT'

fileNamesList = os.listdir('./DDT')

file_names_dict = {}


for fileName in fileNamesList:

    key = int(extractNumber(fileName=fileName))

    fileNameArr = []
    fileNameArr.append(fileName)

    try:
        if file_names_dict[key] != None:
            file_names_dict[key].append(fileName)
    except:
        file_names_dict[key] = fileNameArr


# with open("file_names_dict.txt", "w") as f:
#     f.write(file_names_dict)

searchWords314 = ['tel.', 'preavviso', 'Preavviso', "Tel."]
searchWords318 = ['idraulica', 'Idraulica']

###
# For 314
doesnNotContainArr314 = doesntContainWordsArr(
    contains314Arr, searchWords314, pdfFolder, file_names_dict)

doesnNotContainArr314 = list(set(doesnNotContainArr314))

with open("314Dicembre 2021.txt", "w") as f:
    for string in doesnNotContainArr314:
        f.write(string + '\n')
###


# For 318
doesnNotContainArr318 = doesntContainWordsArr(
    contains318Arr, searchWords318, pdfFolder, file_names_dict)

doesnNotContainArr318 = list(set(doesnNotContainArr318))

with open("318Dicembre 2021.txt", "w") as f:
    for string in doesnNotContainArr318:
        f.write(string + '\n')
###
