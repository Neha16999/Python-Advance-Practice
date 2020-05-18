import PyPDF2
import sys

template=PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_op.pdf','wb') as file:
        output.write(file)








# inputs = sys.argv[1:]    # we are starting from 1 as 0th input will be filename itself
# # print(inputs)       Here it prints list of pdf files that are given as args

# def pdf_combiner(pdf_list):
#     merger=PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         #print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
# pdf_combiner(inputs)
