import time
import os

def Clear_Screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def Write_Line(word, delay=0.1):
    """Prints text with a typewriter effect.
    Args:
        word: The text to display
        delay: Time between characters (default: 0.1s)
    """
    for char in word:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Initialize global variables
listOfOptions = []
numberOfOptions = 0

def New_OptionList():
    """Resets the option list"""
    global listOfOptions, numberOfOptions
    listOfOptions = []
    numberOfOptions = 0

def Add_Option(option):
    """Adds a numbered option to the list"""
    global numberOfOptions, listOfOptions
    numberOfOptions += 1
    listOfOptions.append(f"{numberOfOptions}. {str(option)}")

def Set_Option(word):
    """Adds a non-numbered option to the list"""
    global listOfOptions
    listOfOptions.append(str(word))

def Prompt_Options(prompt="Select an option"):
    """Displays options and gets user choice.
    Args:
        prompt: Custom prompt text (default: "Select an option")
    Returns:
        The selected option number (1-based index)
    """
    if not listOfOptions:
        raise ValueError("No options available to prompt")
    
    print("\nOptions:")
    for option in listOfOptions:
        print(option)
    
    while True:
        try:
            choice = int(input(f"{prompt}: "))
            if 1 <= choice <= len(listOfOptions):
                return choice
            print(f"Please enter a number between 1 and {len(listOfOptions)}")
        except ValueError:
            print("Please enter a valid number.")