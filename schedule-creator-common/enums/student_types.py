from enum import Enum

class StudentTypes(Enum, str):
    BACHELOR = 'bachelor'
    MASTER = 'master'
    PHD = 'phd'