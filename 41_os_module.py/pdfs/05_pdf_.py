from PyPDF2 import PdfMerger
import os

add_pdf = os.listdir()
# print(add_pdf)

# pdfs = ["1.pdf", "2.pdf"]
# print(pdfs)
# print(all_pdf)
merger = PdfMerger()

for pdf in add_pdf:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("result.pdf")
merger.close()
