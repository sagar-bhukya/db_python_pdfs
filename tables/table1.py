from pdf_utils import create_table, get_default_table_style
from reportlab.lib.pagesizes import A4
# def get_table1_data():
#     return [
#         ["Group ID", record['key-name'], "Group Name:", record['key-name']],
#         ["Branch Name (Branch ID)", record['key-name'], "Mobile number", record['key-name']],
#         ["Borrower ID", record['key-name'], "Village/Center Name", record['key-name']],
#         ["Borrower Name", record['key-name'], "F/G/H Name", record['key-name']]
#     ]

# def get_table1_style():
#     return get_default_table_style()

# def draw_table1(c, x, y):
#     data = get_table1_data()
#     col_widths = [135, 135, 135, 135]
#     row_heights = [14, 14, 14, 14]
#     table = create_table(data, col_widths, row_heights, get_table1_style())
#     table.wrapOn(c, *A4)
#     table.drawOn(c, x, y)


from pdf_utils import create_table, get_default_table_style

def get_table_data(record):
    return [
        ["Group ID", record['Loan_ID'], "Group Name", record['MGI_Id']],
        ["Branch Name (Branch ID)", record['MGI_Id'], "Mobile number", record['Mobile Number']],
        ["Borrower ID", record['MBRI_ID'], "Village/Center Name", record["Client's Village's Name"]],
        ["Borrower Name", record["Client's Name"], "F/G/H Name", record["Client's Guardian's Name"]]
    ]

def get_table_style():
    return get_default_table_style()

def draw_table(c, record, x, y):
    data = get_table_data(record)
    col_widths = [135, 135, 135, 135]
    row_heights = [14,14,14,14]
    table = create_table(data, col_widths, row_heights, get_table_style())
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)
