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


def removeStringsWithDash(arr):
    return [x for x in arr if x.find('-') == -1]


def splitByDash(array):
    dividevByDashArr = []

    for x in array:
        if '-' in x:
            split_string = x.split('-')
            for string in split_string:
                dividevByDashArr.append(string)

    return dividevByDashArr


def isSearchWordsContainedInText(wordsArr, text):
    count = 0

    for searchWord in wordsArr:
        if (searchWord in text):
            count += 1

    if count != len(wordsArr):
        return False
    else:
        return True
