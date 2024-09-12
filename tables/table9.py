from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4
from math import ceil

def get_table9_data(temp_py_schedule_data):
    # Dynamically create the rows from 1 to 24
    data9=[
        ["Inst No","Schedule\nDate","Total amt\nDue for Ins\ntallments","Principal","aterest","Closing A\nmount (Pri\nncipal)"],
    ]
    for i, schedule_record in enumerate(temp_py_schedule_data, start=1):
        data9.append([i, schedule_record["Date"], schedule_record['Closing Amount'], schedule_record["Principle Due for the Installment"], schedule_record["ROI"], schedule_record['MLAI_ID']])
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

# def draw_table9(c, temp_py_schedule_data,x, y):
#     data = get_table9_data(temp_py_schedule_data)
#     col_widths = [44.16]*4
#     # row_heights = [35] + [14] * 24
#     row_heights = [35] + [14] * (len(temp_py_schedule_data))  # Adjust heights based on data length
#     table = create_table(data, col_widths, row_heights, get_table9_style())
#     table.wrapOn(c, *A4)
#     table.drawOn(c, x, y)



# def draw_table9(c, temp_py_schedule_data, x_left, x_right, y):
#     # Split the data into two parts (left and right)
#     half = ceil(len(temp_py_schedule_data) / 2)  # First half goes to the left, rest to the right

#     left_data = get_table9_data(temp_py_schedule_data[:half])  # Left half data
#     right_data = get_table9_data(temp_py_schedule_data[half:])  # Right half data

#     # Define column widths and row heights
#     col_widths = [44.16] * 6
#     row_heights_left = [35] + [14] * len(left_data)  # Adjust row heights based on the left data
#     row_heights_right = [35] + [14] * len(right_data)  # Adjust row heights based on the right data

#     # Create left table
#     left_table = create_table(left_data, col_widths, row_heights_left, get_table9_style())
#     left_table.wrapOn(c, *A4)
#     left_table.drawOn(c, x_left, y)  # Draw on the left side

#     # Create right table (with some space between the two tables)
#     right_table = create_table(right_data, col_widths, row_heights_right, get_table9_style())
#     right_table.wrapOn(c, *A4)
#     right_table.drawOn(c, x_right, y)  # Draw on the right side




def draw_table9(c, temp_py_schedule_data, x_left, x_right, y):
    data = get_table9_data(temp_py_schedule_data)
    
    # Split data for left and right tables
    half = (len(data) + 1) // 2  # Split the data approximately in half (rounding up for odd numbers)
    left_data = data[:half]
    right_data = data[half:]
    
    # Define column widths and row heights
    col_widths = [44.16] * 6
    
    # Dynamically create row heights based on the number of rows in each table
    row_heights_left = [35] + [14] * (len(left_data) - 1)
    row_heights_right = [35] + [14] * (len(right_data) - 1)
    
    # Create the left table
    left_table = create_table(left_data, col_widths, row_heights_left, get_table9_style())
    left_table.wrapOn(c, *A4)
    left_table.drawOn(c, x_left, y)
    
    # Create the right table
    right_table = create_table(right_data, col_widths, row_heights_right, get_table9_style())
    right_table.wrapOn(c, *A4)
    right_table.drawOn(c, x_right, y)
