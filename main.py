
from pdf_utils import create_canvas, add_logo, draw_centered_text
from db import execute_procedure, fetch_data_from_db, get_db_connection
from para import down_data
from pdf_utils import get_custom_paragraph_style
from reportlab.platypus import Table, TableStyle,Paragraph
from tables.table1 import draw_table
from tables.table10 import draw_table10
from tables.table2 import draw_table2
from tables.table3 import draw_table3
from tables.table4 import draw_table4
from tables.table5 import draw_table5
from tables.table6 import draw_table6
from tables.table7 import draw_table7
from tables.table8 import draw_table8
from tables.table9 import draw_table9
from tables.table11 import draw_table11
# from reportlab.platypus import Table, TableStyle, Paragraph

def generate_pdfs(mlai_id, branch_id, record, temp_py_schedule_data):
    """
    Function to generate a PDF for a single record.
    """
    # print(temp_py_schedule_data)
    print("--------------")
    filename = f"{branch_id}_{mlai_id}.pdf"
    c, width, height = create_canvas(filename)
    # print(height,"HHHHHHHHHHHHHHHHHHHHH--------")
    add_logo(c, "logo.jpeg", x=30, y=height - 50)
    draw_centered_text(c, "LOAN CARD FACTSHEET", height - 60, width)

    # Draw CIN Number
    c.setFont("Helvetica", 8)
    c.drawString(30, height - 75, "CIN No: U659990R1986PTCO15931")

    # Draw the table for the current record
    draw_table(c, record, 30, height - 150)
    draw_table2(c, record, 30, height - 270)
    draw_table3(c, record, 30, height - 300)
    draw_table4(c, record, 30, height - 328)
    draw_table5(c, record, 30, height - 381)
    draw_table6(c, record, 30, height - 409)
    draw_table7(c, record, 30, height - 602)

    # Finish first page and add a new page
    c.showPage()

    draw_table8(c,30,height-60)
    # # Draw table9 with temp_py_schedule_data on the new page
    # draw_table9(c, temp_py_schedule_data, 30, height - 500)

    # Set positions for left and right tables
    x_left = 30  # Left table starting position
    x_right = 305  # Right table starting position (adjust for spacing)
        # Draw table9 after table8, adjust y position based on previous table
    new_y=draw_table9(c, temp_py_schedule_data, x_left, x_right, height - 70)
    print("new_y1:",new_y)
    print('\n')
    new_y-=120
    # # Now, draw table10 right after table9
    # remaining_y = height - 70 - new_y  # 30 is for padding
    new_y=draw_table10(c, 30, new_y)
    print("new_y2:",new_y)
    print('\n')
    # draw_table10(c, 30, height-400)
    new_y-=78
    new_y=draw_table11(c,30,new_y)
    print("new_y3 :",new_y)
    print('\n')


    #down para draw
    down_para=down_data(a=10)
    custom_style=get_custom_paragraph_style()
    down_p=Paragraph(down_para,custom_style)
    down_p.wrapOn(c,width,height)
    down_p.drawOn(c,30,new_y+160)

    #given font size
    c.setFont("Helvetica", 7)
    c.drawString(30,new_y+140,"Authorized Signatory")
    c.drawString(480,new_y+140,"Borrower Signature ")


    # Save PDF
    c.save()


def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Step 1: Execute procedure to populate temp_py
    execute_procedure("CUST_DOCS_LOANCARD_UPI_Moratorium_NEW_KFSC", "@mlai_id='19882925,19882926,19882930,19882957,19882958'")

    # Step 2: Fetch records from temp_py
    temp_py_records = fetch_data_from_db("SELECT * FROM temp_py")

    # Iterate over each record in temp_py and generate a separate PDF
    for record in temp_py_records:
        mlai_id = record['Loan_ID']  # Access the Loan_ID
        branch_id = record['MGI_Id']  # Access the Branch ID

        # Step 3: Execute Loan_Card24_UPI_Dataset1_KFSC for each mlai_id
        execute_procedure(f"Loan_Card24_UPI_Dataset1_KFSC @mlai_id={mlai_id}")

        # Step 4: Fetch data from Temp_PY_Schedule for this mlai_id
        temp_py_schedule_data = fetch_data_from_db("SELECT * FROM Temp_PY_Schedule")

        # Step 5: Generate PDF for this specific record
        generate_pdfs(mlai_id, branch_id, record, temp_py_schedule_data)

    # Close the database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

