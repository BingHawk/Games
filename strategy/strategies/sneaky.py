from game import Move_enum, Round

def sneaky(history: list[Round])-> Move_enum: 
    if len(history) == 0:
        return Move_enum.cooperate
    
    if len(history) % 11 == 0:
        return Move_enum.defect
    
    return history[-1].opp
        