**Steps**
* python -m venv venv
* activate venv
* pip install -r requiements.txt
* create .env file
```Python
    SECRET_KEY = "YOUR_KEY"  
    ALGORITHM = "YOUR_ALGORITHM"  
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  
    DATABASE_URL = "sqlite+aiosqlite:///./exchange_base.db"  
    EXCHANGE_KEY = "YOUR_API_KEY"
```
* alembic upgrade head
* uvicorn main:app