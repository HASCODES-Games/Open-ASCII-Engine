import time
import src.__init__ as init

def Gameloop():
    """Main game loop function"""
    init.Write_Line("You are now in the game!")
    # Add your game logic here
    time.sleep(2)
    return False  # Return True to continue, False to exit

def game():
    # Initialize game
    init.Write_Line("Welcome to the game!")
    time.sleep(1)
    
    # Reset and set options
    init.New_OptionList()
    init.Set_Option("Start Game")
    init.Set_Option("Exit")
    
    # Get user choice
    choice = init.Prompt_Options()
    
    # Handle choice
    if choice == 1:
        init.Write_Line("Starting the game...")
        time.sleep(1)
        
        # Main game loop
        running = True
        while running:
            pass
            
    elif choice == 2:
        init.Write_Line("Exiting the game...")
        time.sleep(1)
        return
        init.Clear_Screen()

if __name__ == "__main__":
    game()