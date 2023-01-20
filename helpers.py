import os
import PyPDF2


def extractNumber(file):
    try:
        number = file[file.index("-") + 1: file.index("_")]
        return number
    except:
        try:
            number = file[file.index("-") + 1: file.index(" ")]
            return number
        except:
            try:
                number = file[file.index("-") + 1: file.index("-")]
                return number
            except:
                print(file)


def isMatch(name, file):

    if name == extractNumber(file):
        return True
    else:
        return False


def remove_letters(string):
    return ''.join([c for c in string if c.isdigit()])


def removedLettersArr(array):
    new_arr = []
    for string in array:
        new_arr.append(remove_letters(string))
    return new_arr
