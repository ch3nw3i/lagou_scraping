# -*- coding:utf-8 -*-
import xlwt
import json

def read_json(path):
    f = open(path)
    dictory = json.load(f, encoding='utf-8')
    return dictory

if __name__ == '__main__':
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('native')
    sheet.write(0, 0, 'positionName')
    sheet.write(0, 1, 'salary')
    sheet.write(0, 2, 'education')
    sheet.write(0, 3, 'workYear')
    sheet.write(0, 4, 'city')
    sheet.write(0, 5, 'companyShortName')
    sheet.write(0, 6, 'companySize')
    sheet.write(0, 7, 'financeStage')
    sheet.write(0, 8, 'industryField')
    sheet.write(0, 9, 'jobNature')
    sheet.write(0, 10, 'companyLogo')

    sheetPosition = {'row':1, 'col':0}
    pn = 1
    for x in range(pn, 31, 1):
        path = 'd://PyCharmProject//lagou_scraping//Python-' + str(pn) + '.json'
        dictory = read_json(path)
        row = sheetPosition['row']
        col = sheetPosition['col']
        pn = pn + 1
        for x in dictory['content']['positionResult']['result']:
            sheet.write(row, col, x['positionName']) # 0
            col = col + 1
            sheet.write(row, col, x['salary']) # 1
            col = col + 1
            sheet.write(row, col, x['education']) # 2
            col = col + 1
            sheet.write(row, col, x['workYear']) # 3
            col = col + 1
            sheet.write(row, col, x['city']) # 4
            col = col + 1
            sheet.write(row, col, x['companyShortName']) # 5
            col = col + 1
            sheet.write(row, col, x['companySize']) # 6
            col = col + 1
            sheet.write(row, col, x['financeStage']) # 7
            col = col + 1
            sheet.write(row, col, x['industryField']) # 8
            col = col + 1
            sheet.write(row, col, x['jobNature']) # 9
            col = col + 1
            sheet.write(row, col, x['companyLogo']) # 10
            col = col + 1

            col = 0
            row = row + 1
            sheetPosition = {'row': row, 'col': col}
    xls.save('d://PyCharmProject//lagou_scraping//lagou_python.xls')