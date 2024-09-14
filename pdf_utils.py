from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

def create_canvas(filename):
    width, height = A4
    return canvas.Canvas(filename, pagesize=A4), width, height

def add_logo(c, logo_path, x, y, width=90, height=20):
    c.drawImage(logo_path, x=x, y=y, width=width, height=height)

def draw_centered_text(c, text, y_position, page_width, font="Helvetica-Bold", font_size=12):
    c.setFont(font, font_size)
    text_width = c.stringWidth(text, font, font_size)
    x_position = (page_width - text_width) / 2
    c.drawString(x_position, y_position, text)
    c.line(x_position, y_position - 2, x_position + text_width, y_position - 2)

def create_table(data, col_widths, row_heights, style=None):
    table = Table(data, colWidths=col_widths, rowHeights=row_heights)
    if style:
        table.setStyle(style)
    return table

def draw_table(c, table, x, y):
    table.wrapOn(c, *A4)
    table.drawOn(c, x, y)

def get_default_table_style():
    return TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('WORDWRAP', (0, 0), (-1, -1)),  # Enable word wrap in all cells
    ])


# Function to return a custom paragraph style
# Function to get custom paragraph style
def get_custom_paragraph_style():
    styles = getSampleStyleSheet()
    custom_style = styles["Normal"]
    custom_style.fontName = "Helvetica"
    custom_style.fontSize = 5.5  # Set the font size
    custom_style.leading = 7  # Set line spacing (leading)
    custom_style.underline = True  # Set underline
    custom_style.align="TOP"
    custom_style.alignment = 0  # Left alignment
    # custom_style.leftIndent = 0  # Remove any left indent
    custom_style.spaceBefore = 0  # No space before paragraph
    # custom_style.spaceAfter = 0   # No space after paragraph

    return custom_style



# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table, TableStyle
# from reportlab.lib import colors

# def create_canvas(filename, large_page=False):
#     width, height = A4
#     large_height = 2 * height if large_page else height
#     return canvas.Canvas(filename, pagesize=(width, large_height)), width, large_height

# def add_logo(c, logo_path, x, y, width=70, height=30):
#     c.drawImage(logo_path, x=x, y=y, width=width, height=height, mask='auto')

# def draw_centered_text(c, text, y_position, page_width, font="Helvetica-Bold", font_size=12):
#     c.setFont(font, font_size)
#     text_width = c.stringWidth(text, font, font_size)
#     x_position = (page_width - text_width) / 2
#     c.drawString(x_position, y_position, text)
#     c.line(x_position, y_position - 2, x_position + text_width, y_position - 2)

# def create_table(data, col_widths, row_heights, style=None):
#     table = Table(data, colWidths=col_widths, rowHeights=row_heights)
#     if style:
#         table.setStyle(style)
#     return table

# def draw_table(c, table, x, y):
#     table.wrapOn(c, *A4)
#     table.drawOn(c, x, y)

# def get_default_table_style():
#     return TableStyle([
#         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#         ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
#         ('FONTSIZE', (0, 0), (-1, -1), 8),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ])
