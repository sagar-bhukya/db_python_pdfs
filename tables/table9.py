from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pdf_utils import create_table
from reportlab.lib.pagesizes import A4
from math import ceil

def get_table9_data(temp_py_schedule_data):
    # Dynamically create the rows from 1 to 24
    data9=[
        ["Inst No","Schedule\nDate","Total amt\nDue for\nInstallments","Principal","Interest","Closing\nAmount\n(Principal)"],
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
        ('FONTSIZE', (0, 0), (-1, -1), 5.5),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('LEADING', (0,0), (-1,-1),7), # for line spacing
        # ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
        # ('ALIGN', (0, 0), (0, 0), 'CENTER')
]))



# def draw_table9(c, temp_py_schedule_data, x_left, x_right, y):
#     data = get_table9_data(temp_py_schedule_data)

#     # Split data for left and right tables, keeping the header for both tables
#     header = data[0]  # Column headers
#     total_records = len(data) - 1  # Exclude the header from total records count
#     print("total_records : ",total_records)
#     print('\n')

#     # Calculate half size (left side has extra record if odd)
#     half = (total_records + 1) // 2  # Round up for odd numbers
#     print("half :",half)
#     print('\n')

#     left_data = [header] + data[1:half+1]  # Left table data
#     print("left_data :",left_data)
#     print('\n')

#     right_data = [header] + data[half+1:]  # Right table data
#     print("right_data :",right_data)

#     print('\n')

#     # Define column widths
#     col_widths = [44.16] * 6
#     print("length of left data : ",len(left_data))
#     print('\n')
#     print("length of left data",len(right_data))
#     print('\n')

#     # Calculate row heights based on the number of rows in each table
#     row_heights_left = [35] + [14] * (len(left_data) - 1)
#     row_heights_right = [35] + [14] * (len(right_data) - 1)

#     print("row_heights_left :",row_heights_left)
#     print('\n')
#     print("row_heights_right :",row_heights_right)
#     print('\n')
#     left_table = create_table(left_data, col_widths, row_heights_left, get_table9_style())
#     print("left_table :",left_data)
#     print("\n")
#     left_table.wrapOn(c, *A4)
#     left_table.drawOn(c, x_left, y)

#     # Create and draw the right table
#     right_table = create_table(right_data, col_widths, row_heights_right, get_table9_style())
#     print("right_table :",right_data)
#     right_table.wrapOn(c, *A4)
#     right_table.drawOn(c, x_right, y)  # Adjusted y position for the right table



def draw_table9(c, temp_py_schedule_data, x_left, x_right, initial_y):
    """
    Draws the left and right tables with calculated row heights.
    """
    data = get_table9_data(temp_py_schedule_data)

    # Split data for left and right tables, keeping the header for both tables
    header = data[0]  # Column headers
    total_records = len(data) - 1  # Exclude the header from total records count

    # Calculate half size (left side has extra record if odd)
    half = (total_records + 1) // 2
    print("half :",half)
    print('\n')


    left_data = [header] + data[1:half+1]  # Left table data
    right_data = [header] + data[half+1:]  # Right table data

    # Define column widths
    col_widths = [30]+[58.32]+[44.16] * 4
    print(col_widths)

    # Calculate row heights based on the number of rows in each table
    row_heights_left = [25] + [14] * (len(left_data) - 1)
    row_heights_right = [25] + [14] * (len(right_data) - 1)

    # Calculate the total height consumed by the tables
    total_height_left = sum(row_heights_left)
    print("total_height_left :",total_height_left)
    print('\n')
    total_height_right = sum(row_heights_right)
    print(total_height_right)
    # The y position after accounting for the space consumed by previous content
    current_y_left = initial_y - total_height_left
    current_y_right = initial_y - total_height_right

    # Create and draw the left table
    left_table = create_table(left_data, col_widths, row_heights_left, get_table9_style())
    left_table.wrapOn(c, *A4)
    left_table.drawOn(c, x_left, current_y_left)

    # Create and draw the right table
    right_table = create_table(right_data, col_widths, row_heights_right, get_table9_style())
    right_table.wrapOn(c, *A4)
    right_table.drawOn(c, x_right, current_y_right)
    print("min(current_y_left, current_y_right)---:",min(current_y_left, current_y_right))

    # Return the lowest Y position reached by either table to know where to continue drawing
    return min(current_y_left, current_y_right)