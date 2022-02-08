import pandas as pd
import pdfkit
from jinja2 import Template


data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv",
    delimiter=";"
)

html = '''<html>
    <head>
        <title>Геральдические символы Москвы</title>
        <meta charset="utf-8"/>
    </head>
<body>'''
for i, item in data.iterrows():
    html += Template(open('heraldic.item.html').read()).render(data=item)
html += '</body></html>'

config = pdfkit.configuration(
    wkhtmltopdf='C:/Program FIles/wkhtmltopdf/bin/wkhtmltopdf.exe'
)

options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'heraldic.pdf', configuration=config, options=options)
