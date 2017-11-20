from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import pandas as pd
import numpy as np
import re, copy
import ntpath

from os import listdir
from os.path import isfile, join



# parsing pdf
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()

    output.close
    return text

mypath = './data'

# array of titles
titleArr = ['Positionskennzahlen', 'PORTFOLIO CHARACTERISTICS']

# get the absolute url of pdf files
files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

# open output file
csv = open('output/csvfile.csv', 'w')

# defile header of csv file
df = pd.DataFrame(data=np.array([['File Name'], ['Title'], ['Status'], ['Field']]).transpose())
# save header
df.to_csv(csv, sep=',', index=False, header=False)

# get search results of all pdf file in data directory
for filename in files:

    # parsing one pdf file
    # return value is string value
    text = convert(filename)

    # split pdf string value by '\n'
    textArr = text.split('\n')

    # remove \xc2\a0 and \x0c
    for i in range(0, len(textArr)):
        if i < (len(textArr)-1):
            if re.match(r'[\xc2\a0]', textArr[i]):
                if textArr[i+1] == '':
                    del textArr[i]
                    i -= 1
            else:
                textArr[i] = re.sub(r'[\x0c]', '', textArr[i])

    # convert textArr to numpy arrary
    arr = np.array(textArr)

    for title in titleArr:

        # search title
        # return value is integer
        titleIndex = np.asarray(np.where(arr==title))

        # when title is not found
        if titleIndex.size == 0:
            print('Title not found in '+filename+': ', title)

            df = pd.DataFrame(data=np.array([[ntpath.basename(filename)], [title], ['Title not found']]).transpose())
            df.to_csv(csv, sep=',', index=False, header=False)
            continue

        # if title exists
        titleIndex = int(titleIndex[0])

        textIndexArr = np.where(arr=='')[0]

        # get table datas indices after index of current title
        tableDataIndexArr_tmp = np.where(textIndexArr>titleIndex)[0]

        # variable that calculates table rows count
        diffVal = 0
        i = 0

        # max count of table columns
        deep = 5
        tableDataIndexArr = []
        prevTextIndexVal = 0
        tableDataIndexArr.append(titleIndex + 1)

        for index in tableDataIndexArr_tmp:
            if i == 0:
                textIndexVal = int(textIndexArr[index])
                # calculate count of talbe rows
                diffVal = textIndexVal - int(titleIndex) - 1

                i += 1
                tableDataIndexArr.append(textIndexVal)
                prevTextIndexVal = textIndexVal + 1
            else:
                # fetch columns data of table

                textIndexVal = int(textIndexArr[index])
                if diffVal == (textIndexVal - prevTextIndexVal):
                    tableDataIndexArr.append(prevTextIndexVal)
                    tableDataIndexArr.append(textIndexVal)
                    prevTextIndexVal = textIndexVal + 1
                else:
                    prevTextIndexVal = textIndexVal + 1
            i += 1
            if i > deep:
                break


        # output table data

        tableData = []
        for i in range(0, len(tableDataIndexArr), 2):
            tableData.append(textArr[tableDataIndexArr[i]:tableDataIndexArr[i+1]])

        tableData = [np.full((diffVal), ntpath.basename(filename))] + [np.full((diffVal), title)] + [np.full((diffVal), 'OK')] + tableData

        df = pd.DataFrame(data=np.array(tableData).transpose())
        print(df)


        df.to_csv(csv, sep=',', index=False, header=False)
