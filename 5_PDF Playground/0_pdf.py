import PyPDF2

with open('dummy.pdf','rb') as file:
    #print(file)
    reader=PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
    page=reader.getPage(0)
    page.rotateClockwise(180)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    #To make changes in the pdf
    with open('tilt.pdf','wb')as file1:
        writer.write(file1)
