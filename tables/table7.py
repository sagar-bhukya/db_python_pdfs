from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table7_data(record):
    return [
    ["","","One-time\nRecurring","Amount(in ) or Percenta\nge(%) as applicable","One-time/R\necurring","Amount(in ) or Percenta\nge(%) as applicable"],
    ["(i)","Insurance charges","","","",""],
    ["(ii)","Ingurance charges","","","",""],
    ["(iii)","Spouse Insurance charges (Optional) ","","","",""],
    ["(iv)","Valuation fees","","","",""],
    ["(v)","Any other (please specify)","","","",""],
    ["9","Annual Percentage Rate (APR) (%)","","","",""],
    ["10","Details of Contingent Charges (in ₹ or %, as applicable)","","","",""],
    ["(i)","Penal charges, if any, in case of delayed payment","","","",""],
    ["(ii)","Other penal charges, if any","","","",""],
    ["(iii)","Foreclosure charges, if applicable","","","",""],
    ["(iv)","Charges for switching of loans from floating to fixed rate and vice versa","","","",""],
    ["(v)","Any other charges (please specify)","","","",""],

]

def get_table7_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN',(2,6),(5,6)),
        ('SPAN',(1,7),(5,7)),
        ('SPAN',(1,8),(3,8)),
        ('SPAN',(1,9),(3,9)),
        ('SPAN',(1,10),(3,10)),
        ('SPAN',(1,11),(3,11)),
        ('SPAN',(1,12),(3,12)),
        ('SPAN',(4,8),(5,8)),
        ('SPAN',(4,9),(5,9)),
        ('SPAN',(4,10),(5,10)),
        ('SPAN',(4,11),(5,11)),
        ('SPAN',(4,12),(5,12)),
        
]))

def draw_table7(c,record, x, y):
    data = get_table7_data(record)
    col_widths = [30,210,50,100,50,100]
    row_heights = [25,14,14,14,14,14,14,14,14,14,14,14,14]
    table = create_table(data, col_widths, row_heights, get_table7_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
