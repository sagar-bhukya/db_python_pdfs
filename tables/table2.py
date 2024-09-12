from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table2_data(record):
    return [
        ["1","Loan application No", record['Loan_ID'], "Type of Loan", " "],
        ["2","Sanctioned Loan amount (in Rupees)", " "],
        ["3","Disbursal schedule", ""],
        ["4","Loan term (year/months/days)", " "],
        ["5","nstalment details", ""]
    ]

def get_table2_style():
    return (TableStyle([
        # ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        # ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        # ('BOTTOMPADDING', (0, 0), (-1, 0),8),
        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # ('LINEBEFORE', (1, 2), (1, 2), 0, colors.white), # Remove vertical line before the 2nd column of the 3rd row
        # ('LINEAFTER', (1, 2), (1, 2), 0, colors.white),  # Remove vertical line after the 1st column of the 3rd row
        ('SPAN', (1, 1), (2, 1)),
        ('SPAN', (3, 1), (4, 1)),
        ('SPAN', (1, 2), (2, 2)),
        ('SPAN', (3, 2), (4, 2)),
        ('SPAN', (2, 3), (4, 3)),
        ('SPAN', (1, 4), (3, 4)),
    # ('SPAN', (1, 5), (2, 5)),  # Merge columns 1 and 2 in the 6th row
    # ('SPAN', (3, 5), (4, 5)),  # Merge columns 3 and 4 in the 6th row
        
]))

def draw_table2(c,record,x, y):
    data = get_table2_data(record)
    col_widths = [15, 180, 82.5, 180, 82.5]
    row_heights = [14, 14, 50, 14, 14]
    table = create_table(data, col_widths, row_heights, get_table2_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
