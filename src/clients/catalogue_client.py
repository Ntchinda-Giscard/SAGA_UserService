import httpx
from fastapi import HTTPException, status

class CatalogueClient:
    def __init__(self, base_url: str = "http://localhost:8003"): # Assuming Catalogue runs on 8003
        self.base_url = base_url
    
    def get_route(self, route_id: int):
        try:
            response = httpx.get(f"{self.base_url}/catalogue/routes/{route_id}", timeout=5.0)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            # In a real system, we might want to use a circuit breaker or retry mechanism
            # For now, we assume if we can't reach it, we can't verify, so we fail safe or raise error.
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Catalogue Service Unavailable")
