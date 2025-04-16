import easyocr

reader = easyocr.Reader(['en', 'he'], gpu=False)

def detect_plates(image):
    results = reader.readtext(image)
    plates = []
    for box, text, conf in results:
        cleaned = text.replace(" ", "").replace("-", "")
        if cleaned.isdigit() and 6 <= len(cleaned) <= 9:
            plates.append(text)
    return plates
