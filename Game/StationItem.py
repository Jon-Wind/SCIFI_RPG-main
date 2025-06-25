from abc import ABC, abstractmethod

class StationItem(ABC):
    @abstractmethod
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @abstractmethod
    def examine(self):
        print(self.description) #Activated by the player input command.
