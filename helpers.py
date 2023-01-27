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
    return [x for x in arr if x.find('-') == -1]


def remove_last_letter(string):
    if string[-1].isalpha():
        return string[:-1]
    else:
        return string


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

    return dividevByDashOrSlashArr


def isSearchWordsContainedInText(wordsArr, text):
    count = 0

    for searchWord in wordsArr:
        if (searchWord in text):
            return True

    return False
