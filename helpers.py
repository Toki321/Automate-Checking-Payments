import re


def extractNumber(fileName):
    match = re.search(r"-(\d+)", fileName)
    if match:
        return match.group(1)
    return None


def isMatch(name, file):

    if name == extractNumber(file):
        return True
    else:
        return False


def removeStringsWithDash(arr):
    for string in arr:
        if '-' in string or '/' in string:
            arr.remove(string)

    return arr


def remove_last_letter(string):
    try:
        if not string[-1].isdigit():
            return string[:-1]
        else:
            return string
    except:
        print("string index out of range ", string)


def remove_last_letter_arr(arr):
    arrNew = []

    for x in arr:
        arrNew.append(remove_last_letter(x))

    return arrNew


def remove_after_dash(string):
    if '-' in string:
        return string.split('-')[0]
    else:
        return string


def splitByDashOrSlash(array):
    dividevByDashOrSlashArr = []

    for x in array:
        if '-' in x:
            split_string = x.split('-')
            for string in split_string:
                dividevByDashOrSlashArr.append(string)
        elif '/' in x:
            split_string = x.split('/')
            for string in split_string:
                dividevByDashOrSlashArr.append(string)
        elif '+' in x:
            split_string = x.split('+')
            for string in split_string:
                dividevByDashOrSlashArr.append(string)
        else:
            dividevByDashOrSlashArr.append(x)

    return dividevByDashOrSlashArr


def isSearchWordsContainedInText(wordsArr, text):
    count = 0

    for searchWord in wordsArr:
        if (searchWord in text):
            return True

    return False


arr = removeStringsWithDash(['2204696-2204697', '23322'])

print(arr)
