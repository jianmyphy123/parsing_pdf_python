# -*- coding: utf-8 -*-
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import pandas as pd
import numpy as np

from scrapy.selector import Selector


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

titleArr = ['Positionskennzahlen']

text = convert('./data/FSD_LU1495639202_SWC_CH_de.pdf')
textArr = text.split('\n')

arr = np.array(textArr)
textIndexArr = np.where(arr=='')[0]

titleIndex = int(np.where(arr==titleArr[0])[0])

tableDataIndexArr_tmp = np.where(textIndexArr>titleIndex)[0]

diffVal = 0
i = 0
tableDataIndexArr = []
prevTextIndexVal = 0
tableDataIndexArr.append(titleIndex + 1)
for index in tableDataIndexArr_tmp:
    if i == 0:
        textIndexVal = int(textIndexArr[index])
        diffVal = textIndexVal - int(titleIndex) - 1
        i += 1
        tableDataIndexArr.append(textIndexVal)
        prevTextIndexVal = textIndexVal
        continue
    textIndexVal = int(textIndexArr[index])
    if diffVal == (textIndexVal - prevTextIndexVal):
        tableDataIndexArr.append(textIndexVal)
        prevTextIndexVal = textIndexVal
    else:
        break

df = pd.DataFrame()
i = 0
tableData = []
for index in tableDataIndexArr:
    if i == 0:
        i += 1
    elif i == 1:
        tableData.append(textArr[tableDataIndexArr[0]:tableDataIndexArr[1]-1])
        i += 1
    else:
        tableData.append(textArr[tableDataIndexArr[i-1]+1:tableDataIndexArr[i]])
        i += 1

df = pd.DataFrame(data=np.array(tableData).transpose())
print(df)

# print(textIndexArr[0][0], textIndexArr[0][1], textIndexArr[0][2])
#
# df = pd.DataFrame({'title': textArr[1:textIndexArr[0][0]], 'value': textArr[textIndexArr[0][1]+1:texttextIndexArr[0][2]]})
# print(df)
#
df.to_csv('output/csvfile.csv', sep=',', index=False, header=False)
df.to_excel('output/excelfile.xlsx', sheet_name='sheet1', index=False, header=False)
