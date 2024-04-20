# backend/app/ocr_service.py

from doctr.models import ocr_predictor

def perform_ocr(image_path):
    """Perform OCR on an image file."""
    # Initialize the OCR predictor
    model = ocr_predictor(pretrained=True)
    
    # Read the image file
    with open(image_path, 'rb') as img_file:
        image = img_file.read()

    # Perform OCR
    result = model([image])
    
    # Extract text
    extracted_text = result.summary()
    
    return extracted_text
