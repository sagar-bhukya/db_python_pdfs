from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table9_data():
    # Dynamically create the rows from 1 to 24
    data9=[
        ["Inst No","Schedule\nDate","Total amt\nDue for Ins\ntallments","Principal","aterest","Closing A\nmount (Pri\nncipal)"],
    ]
    for i in range(1, 25):
        data9.append([i, "", "", "", "", ""])
    return data9

def get_table9_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center align 'Inst No' (first column) except the header
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
        # ('ALIGN', (0, 0), (0, 0), 'CENTER')
]))

def draw_table9(c, x, y):
    data = get_table9_data()
    col_widths = [44.16]*4
    row_heights = [35] + [14] * 24
    table = create_table(data, col_widths, row_heights, get_table9_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
