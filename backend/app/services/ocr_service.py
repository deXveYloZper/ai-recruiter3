# backend/app/ocr_service.py

from doctr.models import ocr_predictor
import asyncio
from PIL import Image
import io

async def perform_ocr(image_bytes):
    """Perform OCR asynchronously on an image bytes."""
    loop = asyncio.get_event_loop()
    
    # Initialize the OCR predictor
    model = ocr_predictor(pretrained=True)
    
    # Convert bytes to PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Run OCR using executor to avoid blocking the event loop
    extracted_text = await loop.run_in_executor(None, model, [image])
    
    # Extract text - assuming result structure adjustment according to actual return
    return extracted_text.summary()
