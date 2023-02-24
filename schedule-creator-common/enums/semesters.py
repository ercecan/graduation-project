from enum import Enum

class Semesters(Enum, str):
    FALL = 'fall'
    SPRING = 'spring'
    SUMMER = 'summer'
    FALL_AND_SPRING = 'fall_and_spring'
    ALL = 'all'