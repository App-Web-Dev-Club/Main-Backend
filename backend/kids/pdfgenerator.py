
import io
import datetime
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_permission_pdf(users,code):
    buffer = io.BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    bold_style = styles["Normal"]
    bold_style.fontName = "Helvetica-Bold"

    # Page template content using canvas
    def add_page_template(canvas, doc):
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        year = datetime.date.today().strftime("%Y")
        logo_path = BASE_DIR / "kids/images/KH_Logo.png"
        stamp_path = BASE_DIR / "kids/images/stamp.png"

        canvas.drawImage(logo_path, x=370, y=710+35, width=180, height=50, mask='auto')
        canvas.drawImage(stamp_path, x=50, y=700+35, width=220, height=60, mask='auto')

        canvas.drawString(60, 650, "From")
        canvas.drawString(60, 650 + 45, f"KITS/KIDS/KH/LR/{year}/{str(code).rjust(3, '0')}")
        canvas.drawString(450, 650 + 45, f"Date: {today_date}")
        canvas.drawString(75, 620 + 10, "Head CTC/KIDS,")
        canvas.drawString(75, 595 + 20, "Karunya Institute of Technology and Sciences.")

        canvas.drawString(60, 550 + 30, "To")
        canvas.drawString(75, 520 + 40, "The Chief Warden (Boys Hostel),")
        canvas.drawString(75, 495 + 50, "Karunya Institute of Technology and Science,")
        canvas.drawString(75, 470 + 60, "Coimbatore-641114")

        canvas.drawString(60, 425 + 70, "Subject")
        canvas.drawString(75, 395 + 80, "Re: Permission for late residence entry")

        canvas.drawString(60, 350 + 90, "Respected Sir,")
        canvas.drawString(75, 320 + 100, f"The following students were working late at CTC on {today_date} Till 7:30 PM.")
        canvas.drawString(75, 300 + 105, "Kindly permit them to enter the hostel.")

    # Table content using Platypus
    default_width = 130
    elements.append(Spacer(1, 400))
    table_data = [['SI No.', 'Name', 'Reg No.']]
    for index, user in enumerate(users, start=1):
        name = user['regno']['user']['name']
        register_no = user['regno']['register_no']
        table_data.append([index, name, register_no])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table = Table(table_data, style=table_style)
    table.wrap(doc.width, doc.bottomMargin)
    table_height = table._height
    print(table_height)
    elements.append(table)
    
    sign = ParagraphStyle(
        name='sign',
        fontName='Helvetica',
        fontSize=10,
        textColor="black",
        alignment=2,
        spaceBefore=50,
    )

    thank = ParagraphStyle(
        name='thank',
        fontName='Helvetica',
        fontSize=10,
        textColor="black",
        alignment=1,
        spaceBefore=20,
    )
    
    thank_you_message = "Thank You."
    hod_signature = "(HOD CTC/KIDS)"
    elements.append(Paragraph(thank_you_message, thank))
    elements.append(Paragraph(hod_signature, sign))
    # Build the PDF
    doc.build(elements, onFirstPage=add_page_template)

    buffer.seek(0)
    return buffer


# Usage:
# users = [{'regno': {'user': {'name': 'John Doe'}, 'register_no': 'KT1234'}}, ...]  # Example data
# pdf_buffer = generate_permission_pdf(users)
# Now you can use the 'pdf_buffer' to save the PDF to a file or send it via email
