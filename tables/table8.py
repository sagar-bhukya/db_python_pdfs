from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table8_data():
    return [
    ["LoanRepayment schedule"]
]

def get_table8_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'CENTER')
]))

def draw_table8(c, x, y):
    data = get_table8_data()
    col_widths = [540]
    row_heights = [25]
    table = create_table(data, col_widths, row_heights, get_table8_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
