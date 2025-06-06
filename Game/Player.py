

class Player:
    def __init__(self, name, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0):
        self.name = name
        self.location = current_location
        self.has_tool = has_tool
        self.has_crystal = has_crystal
        self.score = score
        self.hazard_count = hazard_count
    
    def move(self, direction):
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"You move {direction}.")
            self.location.describe()
        else:
            print("You cannot move in that direction.")

    def pick_up_tool():
        if location.has_tool:
            location.remove_tool()
            self.has_tool = True
            print("You have picked up the diagnostic tool.")

    def use_tool_on_droid():
        if has_tool and location.droid_present:
            location.set_droid_present()
            print("You have used the diagnostic tool on the droid.")
        elif has_tool and not location.droid_present:
            print("There is no droid to use the diagnostic tool on.")
        else:
            print("You do not have a diagnostic tool.")

    def pick_up_crystal():
        if location.has_crystal:
            location.remove_crystal()
            self.has_crystal = True
            print("You have picked up the energy crystal.")

    def get_status():
        print(f"Name: {self.name}")
        print(f"Location Name: {self.location.name}")
        print(f"Has Tool: {self.has_tool}")
        print(f"Has Crystal: {self.has_crystal}")
        print(f"Score: {self.score}")
        print(f"Hazard Count: {self.hazard_count}")

