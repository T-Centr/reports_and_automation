import requests
import json
import pandas as pd
import binascii
import pdfkit
from jinja2 import Template


with open('libraries.png', 'rb') as file:
    img = 'data:image/png;base64,' + binascii.b2a_base64(
        file.read(), newline=False).decode("UTF-8")

r = requests.get(
    "https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json"
)

data = pd.DataFrame(json.loads(r.content), columns=[
    "NumOfVisitors", "CommonName"]).fillna(value=0)
data.columns = ["Посетители", "Название"]
data.set_index("Название", inplace=True)
html_template = '''<html>
<head>
    <title>Итоговая таблица по библиотекам</title>
    <meta charset="utf-8"/>
</head>
<body>
    <h1>Распределение посетителей</h1>
    <img src="{{data.image}}" alt="Распределение посетителей">
    <h2>Данные по библиотекам</h2>
    {{data.table}}
</body>
</html>'''

html = Template(html_template).render(data={
    'image': img,
    'table': data.to_html()
})

config = pdfkit.configuration(
    wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(
    html, 'libraries.total.pdf', configuration=config, options=options
)
