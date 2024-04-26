# backend/app/services/data_integration_client.py
import httpx
from fastapi import HTTPException

class BaseAPIClient:
    """Base client for making API requests to external services."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url)

    async def get(self, endpoint: str, params: dict = None):
        """Send a GET request to the specified endpoint."""
        try:
            response = await self.client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Connection error: {str(e)}")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch data")

    async def close(self):
        """Close the HTTP client session."""
        await self.client.aclose()
