from gamecontroller import GameController

def main():
    """
    Main entry point for the SCI-FI RPG game.
    Initializes the game controller and starts the game.
    """
    try:
        # Create and start the game
        game = GameController()
        game.setup_world()
        game.start_game()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("The game will now exit.")
    finally:
        print("\nThank you for playing the WELCOME TO THE SCI-FI RPG game!")

if __name__ == "__main__":
    main()