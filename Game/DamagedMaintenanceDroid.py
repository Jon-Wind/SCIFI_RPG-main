

class DamagedMaintenanceDroid:
    def __init__(self, blocking=True):
        self.blocking = blocking

    def repair(self):
        self.blocking = False
        print("You have repaired the droid.")
    
    def is_blocking(self):
        if self.blocking:
            print("The droid is blocking your path.")
            return True
        else:
            print("The droid is not blocking your path.")
            return False