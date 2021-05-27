from PyPDF2 import PdfFileReader

filename = "z.pdf"
pdf = PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print(page.extractText())
