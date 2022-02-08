import pdfkit


config = pdfkit.configuration(
    wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
)
pdfkit.from_url("https://airee.cloud", "airee.pdf", configuration=config)
pdfkit.from_string(
    '''<html><head><title>Отчет</title><meta charset="utf-8"/></head><body>
    <h1>Пример отчета</h1></body></html>''', 'out.pdf', configuration=config
)
