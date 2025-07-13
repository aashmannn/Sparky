from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./walmart_esg.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Walmart ESG Carbon Optimizer"
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # File upload
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB
    
    # ML Model settings
    MODEL_CACHE_DIR: str = "models"
    FORECAST_HORIZON_DAYS: int = 90
    
    # External APIs
    EPA_API_KEY: Optional[str] = None
    CARBON_PRICE_API_URL: str = "https://api.carbonprice.com/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 