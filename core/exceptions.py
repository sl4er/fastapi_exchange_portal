from fastapi import HTTPException, status

class ExchangeException(HTTPException):
    status_code = 502
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
        
       
class RegistrationException(ExchangeException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Login or email is already exist"
        

class InvalidLoginException(ExchangeException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Invalid login"
  
  
class InvalidPasswordException(ExchangeException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Incorrect password"


class SimilarCurrencyException(ExchangeException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="First currency must be different from second currency"
    
    
class EmptyCurrencyListException(ExchangeException):
    status_code=status.HTTP_200_OK
    detail="List of available currencies is empty"


class ExchangeCurrencyListException(ExchangeException):
    status_code=status.HTTP_200_OK
    detail="Error while trying to exchange valutes"


class JWTUserValidationException(ExchangeException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Could not validate credentials"
    headers={"WWW-Authenticate": "Bearer"}


class JWTTokenExpiredException(ExchangeException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Jwt token is expired"
    headers={"WWW-Authenticate": "Bearer"}
    
    
class JWTTokenErrorException(ExchangeException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Jwt token error"
    headers={"WWW-Authenticate": "Bearer"}


class PasswordValidateException(ExchangeException):
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    detail="Incorrect password (must contain minimum 8 symbols)"
    

class EmailValidateException(ExchangeException):
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    detail="Incorrect email value"
    
class UsernameValidateException(ExchangeException):
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    detail="Incorrect name value (must contain 4 - 20 symbols)"