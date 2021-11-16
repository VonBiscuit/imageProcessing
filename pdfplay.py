import PyPDF4
import sys

# with open('dummy.pdf','rb') as file:
#     reader = PyPDF4.PdfFileReader(file)
#     page = reader.getPage(0)
#     print(page.rotateClockwise(90))
#     writer =PyPDF4.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)

# inputs = sys.argv[1:]
# def pdf_combine(pdf_list):
#     merger = PyPDF4.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
# pdf_combine(inputs)

inputs = sys.argv[1:]
watermark_pdf = inputs[0]
watermark_instance = PyPDF4.PdfFileReader(watermark_pdf)
watermark_page = watermark_instance.getPage(0)
target_pdf = inputs[1]
pdf_reader = PyPDF4.PdfFileReader(target_pdf)

pdf_writer = PyPDF4.PdfFileWriter()

for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)

    # will overlay the watermark_page on top
    # of the current page.
    page.mergePage(watermark_page)

    # add that newly merged page to the
    # pdf_writer object.
    pdf_writer.addPage(page)

with open('watermarked.pdf', 'wb') as out:
    # writes to the respective output_pdf provided
    pdf_writer.write(out)