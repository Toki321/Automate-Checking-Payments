import os


def december_314():

    f = open("test.txt", "r")

    stringArr = []

    for string in f:
        stringArr.append(string)

    # print(len(stringArr))
    # print(stringArr)

    newStringArr = []

    for i in range(len(stringArr)):
        if '-' in stringArr[i]:
            split_string = stringArr[i].split('-')
            for string in split_string:
                newStringArr.append(string)
        else:
            newStringArr.append(stringArr[i])

    return newStringArr

# main_list = list(set(list_2) - set(list_1))
