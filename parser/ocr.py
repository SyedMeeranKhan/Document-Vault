from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_from_image(img_stream):
    return pytesseract.image_to_string(Image.open(img_stream))
