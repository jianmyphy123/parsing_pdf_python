# -*- coding: utf-8 -*-
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import pandas as pd
import numpy as np
import re, copy

from os import listdir
from os.path import isfile, join




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
titleArr = ['Positionskennzahlen', 'PORTFOLIO CHARACTERISTICS']


files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in files:

    text = convert(filename)

    textArr = text.split('\n')

    for i in range(0, len(textArr)):
        if i < (len(textArr)-1):
            if re.match(r'[\xc2\a0]', textArr[i]):
                if textArr[i+1] == '':
                    del textArr[i]
                    i -= 1
            else:
                textArr[i] = re.sub(r'[\x0c]', '', textArr[i])

    arr = np.array(textArr)
    for title in titleArr:
        titleIndex = np.asarray(np.where(arr==title))
        if titleIndex.size == 0:
            print('Title not found in '+filename+': ', title)
            continue
        titleIndex = int(titleIndex[0])

        textIndexArr = np.where(arr=='')[0]

        tableDataIndexArr_tmp = np.where(textIndexArr>titleIndex)[0]


        diffVal = 0
        i = 0
        deep = 5
        tableDataIndexArr = []
        prevTextIndexVal = 0
        tableDataIndexArr.append(titleIndex + 1)

        for index in tableDataIndexArr_tmp:
            if i == 0:
                textIndexVal = int(textIndexArr[index])
                diffVal = textIndexVal - int(titleIndex) - 1

                i += 1
                tableDataIndexArr.append(textIndexVal)
                prevTextIndexVal = textIndexVal + 1
            else:
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



        tableData = []
        for i in range(0, len(tableDataIndexArr), 2):
            tableData.append(textArr[tableDataIndexArr[i]:tableDataIndexArr[i+1]])


        df = pd.DataFrame(data=np.array(tableData).transpose())
        print(df)

        with open('output/csvfile.csv', 'a') as csv:
            df.to_csv(csv, sep=',', index=False, header=False)
