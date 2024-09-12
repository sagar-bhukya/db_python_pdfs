from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table4_data():
    return [
    ["6","Interestrate(6) andtype(fixedorloatingorhybrid) ","",""],
    ["7","lnformationincaseofFloatingrateofinterest","",""]
]

def get_table4_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN',(2,1),(3,1))
]))

def draw_table4(c, x, y):
    data = get_table4_data()
    col_widths = [70,200,90,180]
    row_heights = [14,14]
    table = create_table(data, col_widths, row_heights, get_table4_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
