from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url : str
    algo = "HS256"
    access_token : str
    
    class Config:
        env_file = '.env'
        
settings = Settings()
