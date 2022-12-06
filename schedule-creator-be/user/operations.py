from models import User
import bcrypt
from config import CONFIG

userDB = {'users': [{'name':'ömer','email':'ömer','password':'hash','student_id':'asdas'}]}
class UserOperations():

    async def create_user(self, user: User):
        user.password = UserOperations.hash_password(user.password)
        userDB['users'].append(user)
        return user

    async def get_user_by_email(self, email: str):
        for user in userDB['users']:
            if user['email'] == email:
                return user
        return None
    
    def verify_password(self, password, hashed_password):
        return UserOperations.hash_password(password) == hashed_password
    
    def hash_password(password: str) -> str:
        """Returns a salted password hash"""
        return bcrypt.hashpw(password.encode(), CONFIG.salt).decode()
