from stationitem import StationItem
"""Found in the Docking Bay and needed to win the game."""

class EnergyCrystal(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
    
    def examine(self):
        print(f"{self.description}")
        return True


