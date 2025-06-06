

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

    def describe(self):
        print(f'You are in the {self.name},  {self.description}')
        if self.has_tool:
            print("You see a diagnostic tool here.")
        if self.has_crystal:
            print("You see an energy crystal here.")
        if self.droid_present:
            print("A maintenance droid blocks the way!")
        
        # Add available exits
        if self.exits:
            exits = ", ".join(self.exits.keys())
            print(f"Exits: {exits}.")

    def remove_tool(self):
        if self.has_tool:
            self.has_tool = False

    def remove_crystal(self):
        if self.has_crystal:
            self.has_crystal = False

    def set_droid_present(self):
        if self.droid_present:
            self.droid_present = False