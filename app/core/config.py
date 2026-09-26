import os
import shutil
from typing import List

from dotenv import load_dotenv
from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings

if not os.path.exists(".env") and os.path.exists(".env.example"):
    shutil.copy(".env.example", ".env")

load_dotenv(".env")
load_dotenv(".env.example")


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI General Chatbot"

    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    @classmethod
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    LIVEKIT_URL: str = "livekit_url"
    LIVEKIT_API_KEY: str = "********"
    LIVEKIT_API_SECRET: str = "********"

    GEMINI_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""
    GOOGLE_CLOUD_PROJECT: str = "agentforge-509705"
    GOOGLE_CLOUD_REGION: str = "us-central1"
    GOOGLE_APPLICATION_CREDENTIALS: str = "service_account.json"

    @model_validator(mode="after")
    def sync_google_keys(self) -> "Settings":
        placeholders = {"********", "your_gemini_api_key", "your_api_key", ""}
        
        key = ""
        for candidate in [
            self.GEMINI_API_KEY,
            self.GOOGLE_API_KEY,
            os.getenv("GEMINI_API_KEY", ""),
            os.getenv("GOOGLE_API_KEY", "")
        ]:
            if candidate and candidate not in placeholders:
                key = candidate
                break

        if key:
            self.GEMINI_API_KEY = key
            self.GOOGLE_API_KEY = key
            os.environ["GEMINI_API_KEY"] = key
            os.environ["GOOGLE_API_KEY"] = key

        if self.GOOGLE_CLOUD_PROJECT:
            os.environ["GOOGLE_CLOUD_PROJECT"] = self.GOOGLE_CLOUD_PROJECT
        if self.GOOGLE_CLOUD_REGION:
            os.environ["GOOGLE_CLOUD_REGION"] = self.GOOGLE_CLOUD_REGION

        if self.GOOGLE_APPLICATION_CREDENTIALS and os.path.exists(self.GOOGLE_APPLICATION_CREDENTIALS):
            abs_credentials_path = os.path.abspath(self.GOOGLE_APPLICATION_CREDENTIALS)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = abs_credentials_path

        if self.QDRANT_HOST in ["your_host", "your_host_here", ""]:
            self.QDRANT_HOST = "localhost"

        return self

    STT_API_URL: str = "http://10.1.2.94:8000/v1/"
    LLM_API_URL: str = "http://10.1.2.94:11434/v1/"
    TTS_API_URL: str = "http://10.1.2.94:3000/api/v1/"
    TTS_API_KEY: str = "********"

    SECRET_KEY: str = "********"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"

    LANGCHAIN_TRACING_V2: bool = 'true'
    LANGSMITH_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGSMITH_API_KEY: str = "********"
    LANGSMITH_PROJECT: str = "agentforge"

    QDRANT_PORT: int = 6333
    QDRANT_HOST: str = "localhost"

    TAVILY_API_KEY: str = "********"
    FIRECRAWL_API_KEY: str = "********"

    class Config:
        env_file = (".env", ".env.example")
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
