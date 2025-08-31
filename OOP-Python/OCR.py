from PIL import Image
import pytesseract

# Input image
image_input = "download.png"

# Open image
image_open = Image.open(image_input)

# Run OCR
text = pytesseract.image_to_string(image_open)

print("Extracted Text:")
print(text)
