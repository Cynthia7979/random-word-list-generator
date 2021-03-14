# Processes formatted excel file into csv. See sources/托福红宝词汇45天突破版.xls
import xlrd
import csv
import argparse
import sys, os


def main():
    words_column = 2
    meanings_column = 3
    word_list_end_identifier = lambda row, sheet: sheet.cell_value(row, words_column) == ''
    workbook_path = './托福红宝词汇45天突破版.xls'
    output_path = './sources/'
    sheet_name = 'Sheet1'

    if len(sys.argv) > 1:
        # Parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('workbook', help='the .xls workbook path')
        parser.add_argument('sheet_name', help='the name of the sheet holding word/meaning data')
        parser.add_argument('--wordscol', help='number of the column holding words, starting from 0')
        parser.add_argument('--meaningscol', help='number of the column holding meanings, in integer')
        parser.add_argument('--end',
                            help='lambda function taking arguments "row" and "sheet" that returns True ' +
                                 'when current row marks the end of useful content. See README.md for details.')
        parser.add_argument('--output', help='output path')
        namespace = parser.parse_args()

        workbook_path, sheet_name = namespace.workbook, namespace.sheet_name
        if namespace.end:
            assert namespace.end.startswith('lambda '), 'End identifier must be a lambda function.'
            word_list_end_identifier = eval(namespace.end)
        if namespace.meaningscol:
            meanings_column = int(namespace.meaningscol)
        if namespace.wordscol:
            words_column = int(namespace.wordscol)

    workbook_name = os.path.basename(workbook_path)[:workbook_path.rfind('.')]
    sheet = xlrd.open_workbook(workbook_path).sheet_by_name(sheet_name)

    row = 0

    with open(os.path.join(output_path, '%s.csv' % workbook_name), mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['word', 'meaning'])
        writer.writeheader()
        while not word_list_end_identifier(row, sheet):
            word = sheet.cell_value(row, words_column)
            meaning = sheet.cell_value(row, meanings_column)
            writer.writerow({'word': word, 'meaning': meaning})
            row += 1


if __name__ == '__main__':
    main()
