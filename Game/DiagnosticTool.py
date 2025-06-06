from StationItem import StationItem

class DiagnosticTool(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
    
    def examine(self):
        print(f"{self.description}")


diagnostic_tool = DiagnosticTool("Diagnostic Tool", "This diagnostic tool seems designed to interface with maintenance droids")
diagnostic_tool.examine()
