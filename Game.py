import time
import os
import sys
from pydub import AudioSegment
from pydub.playback import play

# for playing wav file
def Play_Sound(sound_path):    
    sound = AudioSegment.from_wav(sound_path)
    play(sound)

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
    """Displays options and gets user choice."""
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

def Display_Art(art_path):
    try:
        with open(art_path, "r") as file:
            art = file.read()
            print(art)
    except FileNotFoundError:
        print("Art file not found.")

def New_Line():
    """Prints a newline for spacing."""
    print("\n")

def Quit():
    """Exits the program."""
    sys.exit()
