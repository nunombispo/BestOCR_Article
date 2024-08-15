import tesserocr
import pypdfium2 as pdfium

# print(tesserocr.tesseract_version())  # print tesseract-ocr version
# print(tesserocr.get_languages())  # prints tessdata path and list of available languages

# Load a document
pdf = pdfium.PdfDocument("bill-of-sale.pdf")

# Loop over pages and render
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=5).to_pil()
    # image.show()
    print(tesserocr.image_to_text(image))


# Load a document
pdf = pdfium.PdfDocument("nasa-apollo.pdf")

# Loop over pages and render
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=5).to_pil()
    # image.show()
    print(tesserocr.image_to_text(image))