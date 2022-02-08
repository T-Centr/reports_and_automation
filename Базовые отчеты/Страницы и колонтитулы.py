import pdfkit


config = pdfkit.configuration(
    wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
)

options = {
    'page-size': 'A4',
    'margin-top': '0.5in',
    'margin-right': '0.5in',
    'margin-left': '0.5in',
    'margin-bottom': '0.5in',
    'encoding': 'UTF-8',
    'footer-html': 'footer.html',
    'header-font-name': 'Trebuchet',
    'header-right': '[page]',
    'page-offset': 1
}

pdfkit.from_file(
    "final.html", 'final.pdf', configuration=config, options=options
)
