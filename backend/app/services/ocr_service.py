from doctr.models import ocr_predictor
import asyncio
from PIL import Image, UnidentifiedImageError
import io

async def perform_ocr(image_bytes: bytes) -> str:
    """
    Perform OCR asynchronously on an image represented by bytes.
    
    Args:
    image_bytes (bytes): The image data in bytes on which OCR needs to be performed.

    Returns:
    str: The extracted text from the image or an error message if OCR fails.
    """
    loop = asyncio.get_event_loop()

    try:
        # Convert bytes to a PIL Image
        image = Image.open(io.BytesIO(image_bytes))
    except UnidentifiedImageError:
        return "Failed to identify the image. Please ensure the file is an image and try again."

    try:
        # Initialize the OCR predictor with a pretrained model
        model = ocr_predictor(pretrained=True)
        
        # Run OCR using an executor to avoid blocking the async event loop
        result = await loop.run_in_executor(None, lambda: model([image]))
        
        # Extract text from the result assuming result.summary() provides the desired output
        return result.summary()
    except Exception as e:
        return f"OCR processing failed: {str(e)}"
