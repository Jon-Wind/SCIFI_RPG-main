import os
import platform
import time
from location import Location
from damagedmaintenancedroid import DamagedMaintenanceDroid
from player import Player
from diagnostic_tool import DiagnosticTool
from energycrystal import EnergyCrystal

def clear_screen():
    """Clear the console screen in a cross-platform way"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')
    print("=" * 50)  # Add a separator line after clearing

class GameController:
    def __init__(self):
        self.maintenance_tunnels = None #A specific Location
        self.docking_bay = None #A specific Location
        self.droid = None #Blocks the player at the maintenance tunnel
        self.player = None 
        self.diagnostic_tool = None #Removes the Droid
        self.energy_crystal = None #Required to win the game.
    
    def setup_world(self):
        print('Welcome USER (WILL MODIFIED)')
        # Create locations first
        self.maintenance_tunnels = Location("Maintenance Tunnels", "", {}, True, False, True)
        self.docking_bay = Location("Docking Bay", "", {}, False, True, False)
        
        # Now that both locations exist, set up their connections
        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)

        # Set up game objects
        self.droid = DamagedMaintenanceDroid()
        self.diagnostic_tool = DiagnosticTool("Repair Tool", "This tool can repair the damaged maintenance droid.")
        self.energy_crystal = EnergyCrystal("Energy Crystal", "This energy crystal seems to be a key to the docking bay.")
        self.player = Player("Player", self.maintenance_tunnels, False, False, 0, 0)
    
    def display_header(self):
        """Display the game header with current location"""
        print("=" * 50)
        print(f"SCIFI RPG - Current Location: {self.player.location.name}".center(50))
        print("=" * 50)
        time.sleep(1)
    
    def player_name(self):
        while True:
            name = input("Please enter your name: ")
            if name.strip():
                self.player.name = name
                clear_screen()
                break
            else:
                print("Please enter a valid name.")

    def start_game(self): #Main Game Loop
        clear_screen()
        self.player_name()
        print('\n' + ' ' * 15 + f'WELCOME TO THE SCI-FI RPG GAME!\n\nAGENT DESIGINATION [{self.player.name}]')
        self.display_header()
        self.player.location.describe()

        game_over = False
        while not game_over:
            print("\n" + "-" * 50)
            command = input("What would you like to do? (type 'list' for commands):\n> ").strip()
            
            if command.lower() == 'describe':
                clear_screen()
                self.display_header()
                self.player.location.describe()
            elif command.lower() == 'win':
                game_over = self.check_win_condition()
            else:
                clear_screen()
                self.display_header()
                self.process_input(command)
                
            if not game_over and command.lower() != 'clear':
                # Only show location description if we didn't just clear the screen
                print("\n" + "-" * 50)

    def process_input(self, command): #Uses input from the player
        try:
            #Checks if the command is valid
            command = command.lower().strip()
            
            if command == "list":
                print("\nAvailable Commands:")
                print("-" * 20)
                print("- 'describe' - Describe the current location")
                print("- 'move <direction>' - Move in a direction (e.g., 'move east')")
                print("- 'pick up tool' - Pick up the diagnostic tool")
                print("- 'use tool' - Use the diagnostic tool on a droid")
                print("- 'pick up crystal' - Pick up the energy crystal")
                print("- 'status' - Show your current status")
                print("- 'win' - Try to win the game")
            
            elif command.startswith("move "):
                direction = command[5:].strip()
                if direction in ["north", "south", "east", "west"]: #Only Directions
                    if direction in self.player.location.exits:
                        self.player.move(direction)
                    else:
                        print(f"You can't go {direction} from here.")
                else:
                    print("Please specify a valid direction: north, south, east, or west")
            
            
            elif command == "pick up tool": #Score is given for picking up the tool
                if not self.player.pick_up_tool(): #
                    print("There is no tool here to pick up.")
            
            elif command == "use tool": #More score
                self.player.use_tool_on_droid()
            
            elif command == "pick up crystal": #Score is given for picking up
                if not self.player.pick_up_crystal():
                    print("There is no crystal here to pick up.")
            
            elif command == "status": #Displays current status
                print(self.player.get_status())
            
            elif command == "win":
                pass  # Win condition is checked in the start_game loop
                
            else:
                print("Invalid command. Type 'list' for available commands.")
                
        except Exception as e: #Occurs if command is invalid
            print(f"An error occurred: {e}")

    def check_win_condition(self):
        if self.player.location == self.docking_bay and self.player.has_crystal:
            self.player.score += 30 #Final score adds to 110
            print("\n You have won the game!")
            print(f"Your final score is: {self.player.score} Hazards: {self.player.hazard_count}")
            return True
        return False #Game is Over
    