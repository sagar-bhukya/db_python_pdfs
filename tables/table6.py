from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table6_data(record):
    return [
    ["8","Fee/Charges","",""],
    ["","","Payable to the RE(A)","Payable to a third partv through RE (B)"]
]  

def get_table6_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN',(1,0),(3,0)),
        ('SPAN',(0,1),(1,1)),
        ('ALIGN', (2, 1), (3, 1), 'CENTER')

]))

def draw_table6(c,record, x, y):
    data = get_table6_data(record)
    col_widths = [75,75,220,170]
    row_heights = [14,14]
    table = create_table(data, col_widths, row_heights, get_table6_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
