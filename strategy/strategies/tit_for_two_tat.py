from game import Move_enum, Round

def tit_for_two_tat(history: list[Round])-> Move_enum: 
    if len(history) <= 1:
        return Move_enum.cooperate
    
    if history[-1].opp == Move_enum.defect and history[-2].opp == Move_enum.defect:
        return Move_enum.defect
    
    return Move_enum.cooperate
        