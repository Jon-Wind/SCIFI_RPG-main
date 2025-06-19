

class Player:
    def __init__(self, name, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0):
        self.name = name
        self.location = current_location
        self.has_tool = has_tool
        self.has_crystal = has_crystal
        self.score = score
        self.hazard_count = hazard_count
    
    def move(self, direction):
        if direction in self.location.exits and not self.location.droid_present:
            self.location = self.location.exits[direction]
            print(f"You move {direction}.")
            self.location.describe()
        elif self.location.droid_present:
            print("The droid has blocked your path.")
            self.location.describe()
            self.hazard_count += 1
        else:
            print("You cannot move in that direction.")

    def pick_up_tool(self):
        if self.location.remove_tool():
            self.has_tool = True
            print("You have picked up the diagnostic tool.")
            self.score += 10
            return True
        print("There is no tool to pick up.")
        return False

    def use_tool_on_droid(self):
        if not self.has_tool:
            print("You don't have the diagnostic tool.")
            return False
        if not hasattr(self.location, 'droid_present') or not self.location.droid_present:
            print("There is no droid here to use the tool on.")
            return False
        self.location.droid_present = False
        print("You use the diagnostic tool on the droid. It powers down!")
        self.score += 20
        return True

    def pick_up_crystal(self):
        if self.location.remove_crystal():
            self.has_crystal = True
            print("You have picked up the energy crystal.")
            self.score += 50
            return True
        print("There is no crystal to pick up.")
        return False

    def get_status(self):
        return f"Score: {self.score} Hazards: {self.hazard_count}"

