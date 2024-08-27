from passlib.context import CryptContext


pwt_ext = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class Hashing():
    
    def bcrypt(password: str) -> str:
        return pwt_ext.hash(password)
    
    
    def verify(hashed_password: str, plain_password: str) -> bool:
        return pwt_ext.verify(plain_password, hashed_password)


