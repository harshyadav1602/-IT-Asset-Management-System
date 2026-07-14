import os
from datetime import datetime

from flask import send_file

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)


def generate_pdf(report_title, headers, data, filename):
    """
    Universal PDF Generator
    """

    os.makedirs("exports", exist_ok=True)

    pdf_path = os.path.join("exports", filename)

    doc = SimpleDocTemplate(
        pdf_path,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    heading_style.alignment = TA_CENTER

    normal_style = styles["Normal"]

    elements = []

    # -------------------------------------
    # Project Title
    # -------------------------------------

    elements.append(
        Paragraph(
            "IT Asset Management System",
            title_style
        )
    )

    elements.append(
        Paragraph(
            report_title,
            heading_style
        )
    )

    elements.append(
        Paragraph(
            f"Generated on : {datetime.now().strftime('%d-%m-%Y %I:%M %p')}",
            normal_style
        )
    )

    elements.append(Spacer(1, 0.30 * inch))

    # -------------------------------------
    # Table
    # -------------------------------------

    table_data = []

    table_data.append(headers)

    for row in data:

        table_data.append(list(row))

    table = Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0d6efd")),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("FONTSIZE", (0, 0), (-1, -1), 10),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("TOPPADDING", (0, 0), (-1, 0), 10),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")

    ]))

    elements.append(table)

    elements.append(Spacer(1, 0.30 * inch))

    # -------------------------------------
    # Footer
    # -------------------------------------

    elements.append(

        Paragraph(

            "<b>Developed By:</b> Harsh Yadav",

            normal_style

        )

    )

    doc.build(elements)

    return send_file(

        pdf_path,

        as_attachment=True,

        download_name=filename

    )