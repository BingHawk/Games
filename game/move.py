from enum import Enum

class Move_enum(Enum):
    cooperate: 0
    defect: 1
    
class Round:
    opp: Move_enum
    own: Move_enum
    
    def __init__(self, opp: Move_enum, own: Move_enum): 
        self.opp = opp,
        self.own = own