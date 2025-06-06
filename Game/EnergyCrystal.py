from StationItem import StationItem

class EnergyCrystal(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
    
    def examine(self):
        print(f"{self.description}")


Crystal = EnergyCrystal("Energy Crystal", "This energy crystal seems to be a key to the docking bay.")
Crystal.examine()
