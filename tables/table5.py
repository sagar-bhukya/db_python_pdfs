from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4

def get_table5_data(record):
    return [
    ["Reference\nBenchmark","Benchmark\nrate (%) (B) ","Spread\n(%) (S)","Final rate (%)R =\n(B) + (S)","Reset\nperiodicity\nmoths","","Impact of change in the referencebenchmark\n(For 25 bps change in ‘R’, change in:)",""],
    ["","","","","B","S","EPI(₹)","No.of EPIs"],
    ["","","","","","","",""]
]

def get_table5_style():
    return (TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),#its set the middle of all data
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN',(0,0),(0,1)),
        ('SPAN',(1,0),(1,1)),
        ('SPAN',(2,0),(2,1)),
        ('SPAN',(3,0),(3,1)),
        ('SPAN',(4,0),(5,0)),
        ('SPAN',(6,0),(7,0)),

]))

def draw_table5(c,record, x, y):
    data = get_table5_data(record)
    col_widths = [63.75,63.75,35,63.75,31.875,31.875,100,150]
    row_heights = [25,14,14]
    table = create_table(data, col_widths, row_heights, get_table5_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
