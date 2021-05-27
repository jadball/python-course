from PyPDF2 import PdfFileReader

filename = "pdfs/simple.pdf"
pdf = PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print(page.extractText())
