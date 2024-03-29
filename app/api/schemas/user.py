import re
from pydantic import BaseModel, field_validator

from core.exceptions import EmailValidateException, PasswordValidateException, UsernameValidateException


class User(BaseModel):
    name: str
    email: str
    password: str
    
    
    @field_validator("name")
    def validate_name_length(cls, value):
        if len(value) < 4 or len(value) > 20:
            raise UsernameValidateException
        
        return value
    
    @field_validator("password")
    def validate_password_length(cls, value):
        if len(value) < 8:
            raise PasswordValidateException
        
        return value
    
    @field_validator("email")
    def validate_email(cls, value):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        email = re.fullmatch(email_pattern, value)
        if not email:
            raise EmailValidateException
        
        return value
    
class UserOut(BaseModel):
    name: str
    email: str