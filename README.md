. Game Overview
Your task is to build a minimal text-based RPG in Python. The player must follow a fixed “golden path” and earn points exactly as described below. If the player tries to move past the droid before it is repaired, a hazard counter increases. At the end, the game displays total score and hazards.

Golden Path Steps (in order):

Maintenance Tunnels: Player begins here.

Pick up the Diagnostic Tool (awards +10 points).

Use the Diagnostic Tool on the Damaged Maintenance Droid (awards +20 points) to clear it.

Move to Docking Bay.

Pick up the Energy Crystal (awards +50 points).

Type “win” (from Docking Bay) to complete the mission (awards +30 points).

Hazard Rule:

If the player tries to move east (toward Docking Bay) while the droid is still blocking, increment the hazard counter by 1 and display a “droid blocking” message.