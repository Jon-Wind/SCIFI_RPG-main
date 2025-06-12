from Location import Location
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

    def process_input(self, command):
        pass

    def check_win_condition(self):
        pass



test = GameController()

test.setup_world()
test.start_game()
    