from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import pandas as pd

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


text = convert('./data/MR_CH_en_CH0226976816_YES_2017-09-30.pdf', [1])
textArr = text.split('\n')


df = pd.DataFrame({'title': textArr[1:5], 'value': textArr[15:19]})
df.to_csv('output/csvfile.csv', sep=',', index=False, header=False)
df.to_excel('output/excelfile.xlsx', sheet_name='sheet1', index=False, header=False)
