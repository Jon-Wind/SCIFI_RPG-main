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
        
    def _validate_move_command(self, direction: str) -> tuple[bool, str]:
        """Validate a move command.
        
        Args:
            direction: The direction to move in
            
        Returns:
            tuple: (is_valid, message) where:
                - is_valid: bool indicating if the move is valid
                - message: str with feedback for the player
        """
        if not direction:
            return False, "Please specify a direction to move (e.g., 'move east')."
            
        direction = direction.lower().strip()
        valid_directions = ["north", "south", "east", "west"]
        
        if direction not in valid_directions:
            return False, f"Invalid direction '{direction}'. Please use one of: {', '.join(valid_directions)}"
            
        if not hasattr(self.player, 'location') or not self.player.location:
            return False, "Error: Player location not set."
            
        if direction not in self.player.location.exits:
            available = list(self.player.location.exits.keys())
            return False, f"You can't go {direction} from here. Available exits: {', '.join(available) if available else 'none'}"
            
        return True, ""

    def _validate_pickup_command(self, item_type: str) -> tuple[bool, str]:
        if not hasattr(self.player, 'location'):
            return False, "Error: Player location not set."
            
        if item_type == "tool":
            if not hasattr(self.player.location, 'has_tool') or not self.player.location.has_tool:
                return False, "There is no tool here to pick up."
            if hasattr(self.player, 'has_tool') and self.player.has_tool:
                return False, "You already have the tool."
                
        elif item_type == "crystal":
            if not hasattr(self.player.location, 'has_crystal') or not self.player.location.has_crystal:
                return False, "There is no crystal here to pick up."
            if hasattr(self.player, 'has_crystal') and self.player.has_crystal:
                return False, "You already have the crystal."
                
        else:
            return False, f"Invalid item type: {item_type}"
            
        return True, ""

    def _validate_use_tool_command(self) -> tuple[bool, str]:
        if not hasattr(self.player, 'has_tool') or not self.player.has_tool:
            return False, "You don't have a tool to use."
            
        if not hasattr(self.player, 'location') or not self.player.location:
            return False, "Error: Player location not set."
            
        if not hasattr(self.player.location, 'droid_present') or not self.player.location.droid_present:
            return False, "There's nothing to use the tool on here."
            
        return True, ""

    def _show_help(self) -> None:
        """Display the help message with available commands."""
        print("\nAvailable Commands:")
        print("-" * 50)
        print("- 'describe'        - Describe the current location")
        print("- 'move <direction>' - Move in a direction (north, south, east, west)")
        print("- 'pick up tool'    - Pick up the diagnostic tool")
        print("- 'use tool'        - Use the diagnostic tool on a droid")
        print("- 'pick up crystal' - Pick up the energy crystal")
        print("- 'status'          - Show your current status and score")
        print("- 'list'            - Show this help message")
        print("- 'win'             - Try to win the game")
        print("-" * 50)

    def process_input(self, command: str) -> None:
        if not command or not isinstance(command, str):
            print("Please enter a valid command. Type 'list' for available commands.")
            return
        
        command = command.lower().strip()
    
        try:
            if command == "list":
                self._show_help()
            
            elif command.startswith("move "):
                direction = command[5:].strip()
                is_valid, message = self._validate_move_command(direction)
                if is_valid:
                    self.player.move(direction)
                else:
                    print(message)
                
            elif command == "pick up tool":
                is_valid, message = self._validate_pickup_command("tool")
                if is_valid:
                    self.player.pick_up_tool()
                else:
                    print(message)
                
            elif command == "pick up crystal":
                is_valid, message = self._validate_pickup_command("crystal")
                if is_valid:
                    self.player.pick_up_crystal()
                else:
                    print(message)
                
            elif command == "use tool":
                is_valid, message = self._validate_use_tool_command()
                if is_valid:
                    self.player.use_tool_on_droid()
                else:
                    print(message)
                
            elif command == "status":
                print(self.player.get_status())
            
            elif command == "describe":
                self.player.location.describe()
            
            elif command == "win":
                pass  # Handled in game loop
            
            else:
                print(f"Invalid command: '{command}'. Type 'list' for available commands.")
            
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            if __debug__:  # Only show full traceback in development
                import traceback
                error_msg += f"\n\nDebug info:\n{traceback.format_exc()}"
            print(error_msg)

    def check_win_condition(self):
        if self.player.location == self.docking_bay and self.player.has_crystal:
            self.player.score += 30 #Final score adds to 110
            print("\n You have won the game!")
            print(f"Your final score is: {self.player.score} Hazards: {self.player.hazard_count}")
            return True
        return False #Game is Over
    