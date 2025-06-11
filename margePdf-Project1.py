# Marge pdf file 

#jodi amader file gulo alada folder a thake tahole amra evabe connect korbo
import os
folder = "pdf"
from PyPDF2 import PdfMerger
all_pdf=[
    os.path.join(folder, '1.pdf'),
    os.path.join(folder, '2.pdf'),
    os.path.join(folder, '3.pdf'),
    os.path.join(folder, '4.pdf'),
    os.path.join(folder, '5.pdf'),
    os.path.join(folder, '6.pdf'),
    ]
with PdfMerger() as pdf_marger:
    for newFile in all_pdf:
        pdf_marger.append(newFile)
    pdf_marger.write('update_pdf.pdf')



# jodi amar file gulo onno folder a na thake tahole simple vabe code likhlei hobe 
from PyPDF2 import PdfMerger
all_pdf=['1.pdf', '2.pdf','3.pdf','4.pdf','5.pdf','6.pdf']
with PdfMerger() as pdf_marger:
    for newFile in all_pdf:
        pdf_marger.append(newFile)
    pdf_marger.write('update_pdf.pdf')
