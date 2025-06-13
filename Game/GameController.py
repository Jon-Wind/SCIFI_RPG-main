from Location import Location #Imports everything to work.
from DamagedMaintenanceDroid import DamagedMaintenanceDroid
from Player import Player
from DiagnosticTool import DiagnosticTool
from EnergyCrystal import EnergyCrystal

class GameController:
    def __init__(self):
        self.maintenance_tunnels = None
        self.docking_bay = None
        self.droid = None
        self.player = None
        self.diagnostic_tool = None
        self.energy_crystal = None
    
    def setup_world(self):
        print('Welcome USER (WILL MODIFIED)')
        # Create locations first
        self.maintenance_tunnels = Location("Maintenance Tunnels", "", {}, True, False, True)
        self.docking_bay = Location("Docking Bay", "", {}, False, True, False)
        
        # Now that both locations exist, set up their connections
        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)

        self.droid = DamagedMaintenanceDroid()
        self.diagnostic_tool = DiagnosticTool("Repair Tool", "This tool can repair the damaged maintenance droid.")
        self.energy_crystal = EnergyCrystal("Energy Crystal", "This energy crystal seems to be a key to the docking bay.")
        self.player = Player("Player", self.maintenance_tunnels, False, False, 0, 0)
    
    def start_game(self):
        print('Welcome to the Sci-Fi RPG Game!')
        self.player.location.describe()
        game_over = False
        while not game_over:
            print("What we doing? ('list' for commands) ")
            command = input()
            if command.lower().strip() == 'win':
                game_over = self.check_win_condition()
            else:
                self.process_input(command)

    def process_input(self, command):
        try:
            command = command.lower().strip()
            
            if command == "list":
                print("Available commands:")
                print("- 'move <direction>' - Move in a direction (e.g., 'move east')")
                print("- 'pick up tool' - Pick up the diagnostic tool")
                print("- 'use tool' - Use the diagnostic tool on a droid")
                print("- 'pick up crystal' - Pick up the energy crystal")
                print("- 'status' - Show your current status")
                print("- 'win' - Try to win the game")
            
            elif command.startswith("move "):
                direction = command[5:].strip()
                if direction in ["north", "south", "east", "west"]:
                    if direction in self.player.location.exits:
                        self.player.move(direction)
                    else:
                        print(f"You can't go {direction} from here.")
                else:
                    print("Please specify a valid direction: north, south, east, or west")
            
            elif command == "pick up tool":
                if not self.player.pick_up_tool():
                    print("There is no tool here to pick up.")
            
            elif command == "use tool":
                self.player.use_tool_on_droid()
            
            elif command == "pick up crystal":
                if not self.player.pick_up_crystal():
                    print("There is no crystal here to pick up.")
            
            elif command == "status":
                print(self.player.get_status())
            
            elif command == "win":
                pass  # Win condition is checked in the start_game loop
                
            else:
                print("Invalid command. Type 'list' to see available commands.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_win_condition(self):
        if self.player.location == self.docking_bay and self.player.has_crystal:
            self.player.score += 30
            print("You have won the game!")
            print(f"Your final score is: {self.player.score} Hazards: {self.player.hazard_count}")
            return True
        return False



test = GameController()

test.setup_world()
test.start_game()
    