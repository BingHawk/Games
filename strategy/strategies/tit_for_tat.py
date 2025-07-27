from game import Move_enum, Round

def tit_for_tat(history: list[Round])-> Move_enum: 
    if len(history) == 0:
        return Move_enum.cooperate
    
    return history[-1].opp
        