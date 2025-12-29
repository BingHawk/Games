from .moves import Move_enum

class Round:
    opp: Move_enum
    own: Move_enum
    
    def __init__(self, opp: Move_enum, own: Move_enum): 
        self.opp = opp
        self.own = own