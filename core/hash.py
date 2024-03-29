import asyncio
from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
    @staticmethod
    async def bcrypt(password: str):
        hashed_password = await asyncio.to_thread(pwd_ctx.hash, password)
        return hashed_password
    
    @staticmethod
    async def verify(hashed_password, plain_password):
        verify_result = await asyncio.to_thread(pwd_ctx.verify, plain_password, hashed_password)
        return verify_result
