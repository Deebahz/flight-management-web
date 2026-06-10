from reportlab.platypus import (
    SimpleDocTemplate,
    Table
)

def create_report(data):

    pdf = SimpleDocTemplate(
        "report.pdf"
    )

    table = Table(data)

    pdf.build([table])