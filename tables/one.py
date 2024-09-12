# import pyodbc  # For connecting to SQL Server
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas

# # Function to generate the PDF table for each mlai_id
# def get_table_function(schedule_data, mlai_id):
#     pdf_filename = f"loan_card_{mlai_id}.pdf"
#     c = canvas.Canvas(pdf_filename, pagesize=A4)

#     # Add title for the PDF
#     c.setFont("Helvetica", 12)
#     c.drawString(100, 800, f"Loan Card for mlai_id: {mlai_id}")

#     # Initialize position for the table
#     y_position = 750

#     # Assuming schedule_data is a list of tuples/dictionaries
#     for row in schedule_data:
#         # You can access row data like row['column_name'] or row.attribute if row is a tuple
#         c.drawString(100, y_position, f"Data: {row['Loan_ID']}")  # Replace with actual columns from Temp_PY_Schedule
#         y_position -= 20

#         # If the y_position goes too low, create a new page
#         if y_position < 50:
#             c.showPage()
#             y_position = 750

#     c.save()  # Save the PDF

# # Connect to SQL Server
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                       'Server=DESKTOP-TNVFUGD\\SQLEXPRESS;'
#                       'Database=loan;'
#                       'Trusted_Connection=yes;')

# cursor = conn.cursor()

# # Step 1: Fetch mlai_ids from temp_py table
# cursor.execute("SELECT * FROM temp_py")
# mlai_ids = [row.Loan_ID for row in cursor.fetchall()]

# # Step 2: Loop through each mlai_id
# for mlai_id in mlai_ids:
#     # Execute the stored procedure to fill Temp_PY_Schedule
#     cursor.execute(f"exec Loan_Card24_UPI_Dataset1_KFSC @mlai_id={mlai_id}")
#     print("Hi--------------")

#     # Step 3: Fetch data from Temp_PY_Schedule based on mlai_id
#     cursor.execute(f"SELECT * FROM Temp_PY_Schedule WHERE mlai_id={mlai_id}")
#     schedule_data = cursor.fetchall()

#     # Step 4: Generate PDF for the current mlai_id with schedule data
#     get_table_function(schedule_data, mlai_id)

# # Close the connection
# conn.close()

# # add this code to the above codes for specified files and modify something












import pyodbc
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Database connection setup
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-TNVFUGD\\SQLEXPRESS;'
                      'Database=loan;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()

def execute_procedure(procedure, params=None):
    """
    Helper function to execute a stored procedure.
    """
    query = f"EXEC {procedure}"
    if params:
        query += f" {params}"
    cursor.execute(query)
    connection.commit()

def fetch_data(query):
    """
    Helper function to fetch data from a table as a list of dictionaries.
    """
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]  # Get column names
    return [dict(zip(columns, row)) for row in cursor.fetchall()]  # Return rows as dicts


def create_pdf(mlai_id, temp_py_data, temp_py_schedule_data):
    """
    Function to create a PDF for each mlai_id using data from temp_py and Temp_PY_Schedule.
    """
    filename = f"loan_card_{mlai_id}.pdf"
    pdf = canvas.Canvas(filename, pagesize=A4)

    # Add temp_py data to PDF (Table 1)
    y_position = 750
    pdf.drawString(100, y_position, f"Loan Card Report for MLAI_ID: {mlai_id}")
    y_position -= 30
    for key, value in temp_py_data.items():
        pdf.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20

    # Add Temp_PY_Schedule data to PDF (Table 2)
    y_position -= 20
    pdf.drawString(100, y_position, "Loan Details:")
    y_position -= 30
    for schedule_record in temp_py_schedule_data:
        for key, value in schedule_record.items():
            pdf.drawString(100, y_position, f"{key}: {value}")
            y_position -= 20
        y_position -= 10

    pdf.save()

def main():
    # Step 1: Execute procedure to populate temp_py
    execute_procedure("CUST_DOCS_LOANCARD_UPI_Moratorium_NEW_KFSC", "@mlai_id='19882925,19882926,19882930,19882957,19882958'")

    # Step 2: Fetch records from temp_py
    temp_py_records = fetch_data("SELECT * FROM temp_py")
    print(temp_py_records)
    print("-----------------------------------")

    for record in temp_py_records:
        mlai_id = record['Loan_ID']

        # Step 3: Execute Loan_Card24_UPI_Dataset1_KFSC for each mlai_id
        execute_procedure(f"Loan_Card24_UPI_Dataset1_KFSC @mlai_id={mlai_id}")

        # Step 4: Fetch data from Temp_PY_Schedule for this mlai_id
        temp_py_schedule_data = fetch_data("SELECT * FROM Temp_PY_Schedule")
        print(temp_py_schedule_data)
        print("=========================")

        # Step 5: Generate PDF for each mlai_id
        temp_py_data = dict(record)  # Assuming record is in a dict-like format
        print(temp_py_data)
        print("AAAAAAAAAAAAAAAA--------------------")
        temp_py_schedule_data = [dict(row) for row in temp_py_schedule_data]  # Converting rows to dicts
        create_pdf(mlai_id, temp_py_data, temp_py_schedule_data)

    # Close the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
