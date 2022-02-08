from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image


with open("title.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    print("Число страниц", pdf_reader.getNumPages())
    print("Metadata", pdf_reader.documentInfo)
    print("File Author", pdf_reader.documentInfo["/Author"])
    print("File Creator", pdf_reader.documentInfo["/Creator"])

with open("libraries.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(page_num)
        if '/XObject' in pdf_page['/Resources']:
            xObject = pdf_page['/Resources']['/XObject'].getObject()
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    img = Image.frombytes("RGB", size, data)
                    img.save("image.png")

files = ["title.pdf", "libraries.pdf"]
merger = PdfFileMerger()
for filename in files:
    merger.append(PdfFileReader(open(filename, "rb")))
merger.addMetadata({
    '/Producer': "ITtensive",
    '/Author': "ITtensive",
    '/Creator': "ITtensive Python Advanced - www.ittensive.com",
    '/Copyright': "ITtensive 2019",
    '/Title': "Культурная статистика Москвы"
})
merger.write("report.pdf")
