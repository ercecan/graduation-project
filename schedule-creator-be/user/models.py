from pydantic import BaseModel


class User(object):
    def __init__(self, email, password, name, student_id):
        self.email = email
        self.password = password
        self.name = name
        self.student_id = student_id

class UserIn(BaseModel):
    email: str
    password: str
    remember: bool

class UserRegister(BaseModel):
    email: str
    password: str
    name: str
    student_id: str
