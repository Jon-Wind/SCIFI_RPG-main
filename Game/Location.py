

class Location:
    def __init__(self, name, description, exits, has_tool=False, has_crystal=False, droid_present=False):
        self.name = name #Showed in the Description
        self.description = description #Outputted at the start
        self.exits = exits #Where the player can change location
        self.has_tool = has_tool
        self.has_crystal = has_crystal
        self.droid_present = droid_present
    
    def add_exit(self, direction, other_location):
        self.exits[direction] = other_location

    def describe(self):
        start = f'\nYou are in the {self.name},'
        """Adds details to description based on items present."""
        if self.has_tool:
            start += " There is a diagnostic tool here. "
        if self.has_crystal:
            start += " There is an energy crystal here. "
        if self.droid_present:
            start += "\nThere is also a maintenance droid blocking the way! "
        
        if self.exits:
            exits = ", ".join(self.exits.keys())
            start += f"\n Exits: {exits}."
        
        print(f'{start}')
    def remove_tool(self): #Done through player processes
        if self.has_tool:
            self.has_tool = False
            return True
        return False

    def remove_crystal(self): #Done through player processes
        if self.has_crystal:
            self.has_crystal = False
            return True
        return False

    def set_droid_present(self): #Player uses the tool on the droid removing it
        if self.droid_present:
            self.droid_present = False