

class Location:
    def __init__(self, name, description, exits, has_tool=False, has_crystal=False, droid_present=False):
        self.name = name
        self.description = description
        self.exits = exits
        self.has_tool = has_tool
        self.has_crystal = has_crystal
        self.droid_present = droid_present
    
    def add_exit(self, direction, other_location):
        self.exits[direction] = other_location

    def describe():
        pass

    def remove_tool():
        pass

    def remove_crystal():
        pass

    def set_droid_present(flag):
        pass