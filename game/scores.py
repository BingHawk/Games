class Scores:
    def __init__(self, 
                 DEFECT_DEFECT: int = 1, 
                 DEFECT_COOPERATE: int = 5, 
                 COPERATE_COOPERATE: int = 3, 
                 COOPERATE_DEFECT: int = 0
                 ):
        self.DEFECT_DEFECT = DEFECT_DEFECT
        self.DEFECT_COOPERATE = DEFECT_COOPERATE
        self.COPERATE_COOPERATE = COPERATE_COOPERATE
        self.COOPERATE_DEFECT = COOPERATE_DEFECT