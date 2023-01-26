import numpy as np
import pandas as pd
import os
import PyPDF2

from helpers import splitByDash, removeStringsWithDash


def getArrThatContains314or318(number):

    # Read an Excel file
    df = pd.read_excel('excelFile.xlsx', sheet_name='Giugno 2022')

    # Fill the missing values in the first column with the previous non-null value
    df.iloc[:, 0].fillna(method='ffill', inplace=True)

    # Filter all rows that have 314 or 318 in second column
    if number == 314:
        selectedRows = df.iloc[np.where(df.iloc[:, 1] == 314)]
    else:
        selectedRows = df.iloc[np.where(df.iloc[:, 1] == 318)]

    # Get the first column data for filtered rows
    containsArr = selectedRows.iloc[:, 0]

    # Convert to string
    containsArr = [str(x) for x in containsArr]

    # Get the numbers with dashes in between them and append them to arr
    containsSplitByDashArr = splitByDash(containsArr)
    containsArr.extend(containsSplitByDashArr)

    # Remove the strings with dashes (they were splitted into multiple strings and appended above)
    containsArr = removeStringsWithDash(containsArr)

    # Remove duplicates
    containsArr = list(set(containsArr))

    return containsArr
