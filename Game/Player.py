

class Player:
    def __init__(self, name, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0):
        self.name = name #May be decided by Player
        self.location = current_location #The location the player is
        self.has_tool = has_tool #Assists in removing the Droid
        self.has_crystal = has_crystal #Required to win the game
        self.score = score #Achieved by ingame events.
        self.hazard_count = hazard_count #Achieved by walking into the droid
    
    def move(self, direction): #Checks if a direction exists and moves there.
        if direction in self.location.exits and not self.location.droid_present:
            self.location = self.location.exits[direction]
            print(f"You move {direction}.")
            self.location.describe()
        elif self.location.droid_present:
            print("The droid has blocked your path.")
            self.location.describe()
            self.hazard_count += 1 #Shown at the end of the game

    def pick_up_tool(self): #Can only be done if there is a Tool in the room.
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
        if not hasattr(self.location, 'droid_present') or not self.location.droid_present: #Checks Attribute in Location.
            print("There is no droid here to use the tool on.")
            return False
        self.location.droid_present = False
        self.location.droid.repair()
        print("You use the diagnostic tool on the droid. It powers down!")
        self.score += 20
        return True

    def pick_up_crystal(self): #Only possible in the docks and needed to win.
        if self.location.remove_crystal():
            self.has_crystal = True
            print("You have picked up the energy crystal.")
            self.score += 50
            return True
        print("There is no crystal to pick up.")
        return False

    def get_status(self): #Shows the player's current status.
        return f"Score: {self.score} Hazards: {self.hazard_count}"

