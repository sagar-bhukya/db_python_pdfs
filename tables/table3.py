from pdf_utils import create_table, get_default_table_style
from reportlab.lib.pagesizes import A4
def get_table3_data(record):
    return [
    ["Trpeofinstalment","AumberoiEPIS","EPIE","commencem entof repayment, postsanction"],
    ["","","",""]
]

def get_table3_style():
    return get_default_table_style()

def draw_table3(c,record,x, y):
    data = get_table3_data(record)
    col_widths = [80,80,45,335]
    row_heights = [14,16]
    table = create_table(data, col_widths, row_heights, get_table3_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
