import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())
import cv2
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image = cv2.imread("sample_image.jpg")
if image is None:
    print("Image not found. Check filename and path.")
    exit()
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, threshold = cv2.threshold(
    gray,
    150,
    255,
    cv2.THRESH_BINARY
)

# Extract text
text = pytesseract.image_to_string(threshold)

# Display result
print("Recognized Text:")
print(text)

# Show processed image
cv2.imshow("Processed Image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()