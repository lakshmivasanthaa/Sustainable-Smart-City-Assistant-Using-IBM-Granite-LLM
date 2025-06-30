from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    WATSONX_API_KEY: str
    WATSONX_PROJECT_ID: str
    WATSONX_URL: str
    WATSONX_MODEL_ID: str

    PINECONE_API_KEY: str
    PINECONE_ENV: str
    INDEX_NAME: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
