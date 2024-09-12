
# from pdf_utils import create_canvas, add_logo, draw_centered_text
# from tables.table1 import draw_table1
# from tables.table2 import draw_table2
# from tables.table3 import draw_table3
# import tables
# from db import fetch_data_from_db
# import tables.table4
# import tables.table5
# import tables.table6
# import tables.table7

# def generate_pdf(data):
#     # Create a PDF canvas with default A4 size
#     c, width, height = create_canvas("loan_factsheet.pdf")

#     # First Page Content
#     # Add logo and title on the first page
#     add_logo(c, "sagar_logo.jpeg", x=30, y=height - 50)
#     draw_centered_text(c, "LOAN CARD FACTSHEET", height - 60, width)

#     # Draw CIN Number
#     c.setFont("Helvetica", 8)
#     c.drawString(30, height - 75, "CIN No: U659990R1986PTCO15931")

#     # Draw first page tables
#     draw_table1(c, 30, height - 150)
#     draw_table2(c,30,height-270)
#     draw_table3(c,30,height-300)
#     tables.table4.draw_table4(c,30,height-328)
#     tables.table5.draw_table5(c,30,height-381)
#     tables.table6.draw_table6(c,30,height-409)
#     tables.table7.draw_table7(c,30,height-602)

#     # # Finish first page and add a new page
#     # c.showPage()

#     # # Second Page Content
#     # draw_centered_text(c, "Second Page Header", height - 60, width)

#     # # Draw more tables or other content for the second page
#     # draw_table1(c, 30, height - 150)  # Reusing table1 for example

#     # Save the PDF after completing all pages
#     c.save()

# def main():
#     # Fetch data from the database
#     query = "SELECT * FROM temp_py"
#     data = fetch_data_from_db(query)
#     print(data)  # Debugging

#     # Generate PDF
#     generate_pdf(data)

# if __name__ == "__main__":
#     main()




from pdf_utils import create_canvas, add_logo, draw_centered_text
from tables.table1 import draw_table
from tables.table2 import draw_table2
from db import fetch_data_from_db

def generate_pdfs(records):
    for i, record in enumerate(records):
        #print(record)
        filename = f"loan_factsheet_{i+1}.pdf"
        c, width, large_height = create_canvas(filename, large_page=True)

        # Add logo and title
        add_logo(c, "sagar_logo.jpeg", x=30, y=large_height - 50)
        draw_centered_text(c, "LOAN CARD FACTSHEET", large_height - 60, width)

        # Draw CIN Number
        c.setFont("Helvetica", 8)
        c.drawString(30, large_height - 75, "CIN No: U659990R1986PTCO15931")

        # Draw the table for the current record
        draw_table(c, record, 30, large_height - 150)
        draw_table2(c,record,30,large_height-270)

        # Save PDF
        c.save()

def main():
    # Fetch data from the database
    query = "SELECT * FROM temp_py"
    records = fetch_data_from_db(query)

    # Generate PDFs
    generate_pdfs(records)

if __name__ == "__main__":
    main()