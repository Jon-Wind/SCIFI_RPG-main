To play the game Open up main.py in the Game folder and run it.

CONSTANTS: Keeps all the Story Data that can be easily changed in later verisons. With details like the names of the locations, items all being stored in Constants and being able to be changed.

This is the Golden Path
1) Maintenance Tunnels: Player begins here.
2) Pick up the Diagnostic Tool (awards +10 points).
3) Use the Diagnostic Tool on the Damaged Maintenance Droid (awards +20 points) to clear it.
4) Move to Docking Bay.
5) Pick up the Energy Crystal (awards +50 points).
6) Type “win” (from Docking Bay) to complete the mission (awards +30 points).

Hazard Rule:
If the player tries to move east (toward Docking Bay) while the droid is still blocking, increment the hazard counter by 1 and display a “droid blocking” message.
