from reportlab.platypus import Table, TableStyle,Paragraph
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4
from para import left_side_para,right_side_para
from pdf_utils import get_custom_paragraph_style
def get_table11_data():
    custom_style=get_custom_paragraph_style()
    left_data=left_side_para()
    left_para=Paragraph(left_data,custom_style)

    right_data=right_side_para(a=10,b=20,c=30)
    right_para=Paragraph(right_data,custom_style)
    return [
[left_para,right_para]
]

def get_table11_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        # ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center align 'Inst No' (first column) except the header
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('LEADING',(0,0),(-1,-1), 10),
        # ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
        # ('ALIGN', (0, 0), (0, 0), 'CENTER')
]))

def draw_table11(c, x, y):
    data = get_table11_data()
    col_widths = [270,270]
    row_heights = [185]
    table = create_table(data, col_widths, row_heights, get_table11_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
    return y-sum(row_heights)
