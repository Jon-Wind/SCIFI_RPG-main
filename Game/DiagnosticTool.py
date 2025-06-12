from StationItem import StationItem

class DiagnosticTool(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
    
    def examine(self):
        print(f"{self.description}")


