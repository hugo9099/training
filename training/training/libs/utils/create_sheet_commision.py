from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Style, NumberFormatDescriptor
from openpyxl.styles import colors

from openpyxl.cell import Cell
import datetime

colorMap = {'Chargeback': '00FF0000', 'Terminated': '00CCFFCC', 'Payment': '00CCFFCC'}


def createCommissionAgent(sales, payment_date, branch):
    wb = Workbook()
    ws = wb.active
    ws_sumary = wb.create_sheet()
    ws_sumary.title = "Earnings Summary"

    addcell_value(1, 1, 5, '00FF0000', ws_sumary)
    addcell_value(2, 1, 6, '00CCFFCC', ws_sumary)
    addcell_value(3, 1, "=SUM(A1, A2)", '00FFFFFF', ws_sumary, '0.00%')
    addcell_value(5, 1, payment_date, '00CCFFCC', ws_sumary, data_type='mm/dd/yyyy')
    d_file = payment_date
    filename = '../{}_{}.xlsx'.format(branch, d_file.strftime('%m_%d_%Y'))

    wb.save(filename)


def addcell_value(row, col, data, bg_color, sheet, data_type='#,##0.00', font_size=12, is_bold=True, ):
    cell = sheet.cell(row=row, column=col)
    cell = '{}{}'.format(cell.column, cell.row)
    sheet[cell] = data
    sheet[cell].font = Font(size=12, bold=is_bold)
    sheet[cell].style = Style(fill=PatternFill(patternType='solid', fgColor=Color(bg_color)),
                                  number_format=data_type)



def main():
    createCommissionAgent(sales=[], payment_date=datetime.date.today(), branch='HBC')


if __name__ == '__main__':
    main()
