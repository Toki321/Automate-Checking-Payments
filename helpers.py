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
