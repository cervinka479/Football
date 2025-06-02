from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Config(BaseSettings):
    openai_api_key: SecretStr
    knowledge_base_path: str
    last_run_file: str
    football_base_url: str

    class Config:
        env_file = ".env"  # Load variables from .env file

config = Config()

if __name__ == "__main__":
    print(config.__dict__)

