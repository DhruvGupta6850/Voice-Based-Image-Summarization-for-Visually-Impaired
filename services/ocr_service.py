import easyocr


class OCRService:

    def __init__(self):
        print("Loading OCR model...")
        self.reader = easyocr.Reader(['en'])
        print("OCR model loaded.")

    def extract_text(self, image_path):

        results = self.reader.readtext(
            image_path,
            detail=0
        )

        text = " ".join(results)

        return text


ocr_service = OCRService()