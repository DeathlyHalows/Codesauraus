import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Python_Libraries\tesseract.exe"

def extract_text_from_image_cv2(image) -> str:
    if image is None:
        raise ValueError("Invalid image")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def write_text_to_file(text: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
