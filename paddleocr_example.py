from paddleocr import PaddleOCR, draw_ocr
import pypdfium2 as pdfium
from PIL import Image


# Load a document
pdf = pdfium.PdfDocument("bill-of-sale.pdf")

# Initialize PaddleOCR and load English model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Loop over pages and render
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=5).to_pil()
    image.save(f'image{i}.jpg')

    # OCR the image
    result = ocr.ocr(f'image{i}.jpg', cls=True)
    for idx in range(len(result)):
        res = result[idx]
        # Print the OCR result
        for line in res:
            print(line)

    # Optionally, draw the OCR result on the image
    result = result[0]
    image = Image.open(f'image{i}.jpg').convert('RGB')
    boxes = [line[0] for line in result]
    texts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, texts, scores, font_path='C:\\Windows\\Fonts\\Arial.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(f'result{i}.jpg')
