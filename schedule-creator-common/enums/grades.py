from enum import Enum

class Grades(Enum):
    AA = 'AA'
    BA = 'BA'
    BB = 'BB'
    CB = 'CB'
    CC = 'CC'
    DC = 'DC'
    DD = 'DD'
    FD = 'FD'
    FF = 'FF'

    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __ne__(self, other):
        return self.value != other.value
