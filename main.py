import os
from threading import Thread

from getArrThatContains314or318 import getArrThatContains314or318
from getArrThatDoesntContainNeededWords import doesntContainWordsArr
from helpers import extractNumber, remove_after_dash, remove_last_letter

# "Gennaio 2022", "Febbraio 2022",
sheetNamesArr = ["Marzo 2022",
                 "Aprile 2022", "Maggio 2022", "Giugno 2022", "Luglio 2022"]

sheetNamesLastFiveMonthsArr = ["Agosto 2022",
                               "Settembre 2022", "Orrobre 2022", "Novembre 2022", "Dicembre 2022"]
# "Agosto 2022",

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


for sheetName in sheetNamesLastFiveMonthsArr:

    contains314Arr = getArrThatContains314or318(314, sheetName)

    contains318Arr = getArrThatContains314or318(318, sheetName)

    print(contains314Arr)
    print(contains318Arr)

    # searchWords314 = ['tel.', 'preavviso', 'Preavviso', "Tel."]
    # searchWords318 = ['idraulica', 'Idraulica']

    searchWords314 = ['TEL.', 'PREAVVISO']
    searchWords318 = ['SERVE']

    ###
    # For 314
    doesnNotContainArr314 = doesntContainWordsArr(
        contains314Arr, searchWords314, pdfFolder, file_names_dict)

    doesnNotContainArr314 = list(set(doesnNotContainArr314))

    with open("./final/" + sheetName + " 314.txt", "w") as f:
        for string in doesnNotContainArr314:
            f.write(string + '\n')
    ###

    # For 318
    doesnNotContainArr318 = doesntContainWordsArr(
        contains318Arr, searchWords318, pdfFolder, file_names_dict)

    doesnNotContainArr318 = list(set(doesnNotContainArr318))

    with open("./final/" + sheetName + " 318.txt", "w") as f:
        for string in doesnNotContainArr318:
            f.write(string + '\n')
    ###
