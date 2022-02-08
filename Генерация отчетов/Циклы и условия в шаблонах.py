import pandas as pd
import pdfkit
from jinja2 import Template


data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv",
    delimiter=";"
)

html = Template(
    open('heraldic.html', encoding="utf-8").read()).render(data=data.iterrows())
config = pdfkit.configuration(
    wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
)

options = {
    'page-size': 'A4',
    'header-right': '[page]'
}

pdfkit.from_string(html, 'heraldic.pdf', configuration=config, options=options)
