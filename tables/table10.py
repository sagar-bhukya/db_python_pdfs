from reportlab.platypus import Table, TableStyle,Paragraph
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from para import get_dynamic_paragraph
from pdf_utils import get_custom_paragraph_style

def get_table10_data():
    paragraph_text = get_dynamic_paragraph(
        total_emi=100000, 
        first_emi=5000, 
        instalment_amount=4500, 
        tenure=24, 
        last_instalment=5500, 
        loan_processing_fee=1000, 
        loan_amount=200000, 
        interest_charges=30000
    )
    custom_style=get_custom_paragraph_style()
       # Create a styled paragraph
    paragraph = Paragraph(paragraph_text,custom_style)
    return [
    ["Important Note: "],
    [paragraph],  # Insert the styled paragraph here
    ["Customer Support Service: Toll Free number :18008437200 Timing: 09:30 am to 06:30 pm"]

]

def get_table10_style():
    return (TableStyle([
        # ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        # ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center align 'Inst No' (first column) except the header
        ('FONTSIZE', (0, 0), (0, 1), 5.5),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('ALIGN', (0, 0), (0, 2), 'CENTER'),
        ('VALIGN',(0,0),(0,0),'MIDDLE'),
        ('FONTSIZE', (0, 0), (0, 0), 8),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 0), (0, 2), 'Helvetica-Bold'),
        ('VALIGN',(0,0),(0,2),'MIDDLE'),
        ('FONTSIZE', (0, 0), (0, 2), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
        # ('ALIGN', (0, 0), (0, 0), 'CENTER')
        ('LEADING', (0, 1), (0, 1), 7), # for line spacing
]))

def draw_table10(c, x, y):
    data = get_table10_data()
    col_widths = [540]
    row_heights = [14,80,14]
    table = create_table(data, col_widths, row_heights, get_table10_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
    return y-sum(row_heights)
