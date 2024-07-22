import PyPDF2
files = ["1.pdf","2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in files:
    file = open(filename,'rb')
    reader= PyPDF2.PdfReader(file)
    merger.append(reader)
file.close()
merger.write('merged.pdf')