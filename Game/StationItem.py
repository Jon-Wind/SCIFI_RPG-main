

class StationItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def examine(self):
        print(self.description)
