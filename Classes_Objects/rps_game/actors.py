class Player:
    def __init__(self, name):
        """ class variable Player.name"""
        self.name = name

class roll:
    def __init__(self, roll_name):
        """ class variable roll.roll_name, roll.wins, roll.loss"""
        self.roll_name = roll_name
        self.wins = []
        self.loss = []
   
    def update_roll(self, wins, loss):
        self.wins = wins
        self.loss = loss
    
    def can_defeat(self, roll):
        for item in self.wins:
            if item.roll_name == roll.roll_name:
                return True
        return False
