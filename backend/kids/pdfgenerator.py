import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def generate_permission_pdf(users):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    # Set font and size
    p.setFont("Helvetica", 12)
    

    today_date = datetime.date.today().strftime("%d-%m-%Y")
    logo_path = "/home/jerin/Documents/Development/Main-Backend/backend/kids/images/KH_Logo.png"

    # Write the content to the PDF
    p.drawImage(logo_path, x=50, y=700,width=250,height=70,mask='auto')
    p.drawString(60, 650, "From") 
    p.drawString(450, 650, f"Date: {today_date}")  
    p.drawString(75, 620, "Head CTC/KIDS,")  
    p.drawString(75, 595, "Karunya Institute of Technology and Sciences.")  
    
    p.drawString(60, 550, "To")  
    p.drawString(75, 520, "The Chief Warden (Boys Hostel),")  
    p.drawString(75, 495, "Karunya Institute of Technology and Science,")  
    p.drawString(75, 470, "Coimbatore-641114")  
    
    p.drawString(60, 425, "Subject")  
    p.drawString(75, 395, "Re: Permission for late residence entry") 
    
    p.drawString(60, 350, "Respected Sir,")
    p.drawString(75,320,f"The following students were working late at CTC on {today_date} Till 7:30 PM.")
    p.drawString(75,300,"Kindly permit them to enter the hostel.")

    # The following students were working late at CTC on 12-03-2024 Till 7:30 PM . Kindly permit  them to enter the hostel. 
    data = [['SI No.', 'Name', 'Register No.']]
    for index, user in enumerate(users, start=1):
        name = user['regno']['user']['name']
        register_no = user['regno']['register_no']
        data.append([index, name, register_no])
    
    # Create the table
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    
    # Draw the table on the canvas
    table.wrapOn(p, 500, 500)
    table.drawOn(p, 50, 200)

    table_height = sum(table._rowHeights) + len(table._rowHeights) * 1  # Total height of the table
    y_position = 200 - table_height - 10  # 30 units below the table

    # Calculate the x-coordinate for centering the text
    text_width = p.stringWidth("Thank You.", "Helvetica", 12)
    x_position = (width - text_width) / 2  # Centering based on the canvas width

    # Write closing remarks
    p.drawString(x_position, y_position, "Thank You.")
    p.drawString(width - text_width - 70, 50, "(HOD CTC/KIDS)")
    
    # Save the PDF
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

# Generate the PDF
# pdf_buffer = generate_permission_pdf()


# Now you can use the 'pdf_buffer' to save the PDF to a file or send it via email
