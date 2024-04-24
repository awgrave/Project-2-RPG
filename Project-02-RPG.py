''' 
Aidan Graves
4/16/24
CPSC 1050 Project 2 - RPG

CODE DESCRIPTION:
This is the 2nd project for CPSC 1050. The assignment is to create a RPG video game. My video game is a text based mystery game about 
a disturbing disappearance in a seemingly normal suburban home. 

GITHUB LINK: 
*insert link to repo here*
'''

import pickle #used for saving game data and loading from save files
import os #used for wiping saved data for new playthroughs

Notebook_file = 'Notebook.txt' #uses the variable Notebook_file to reference the .txt
Save_game_data = 'savegame.dat' #uses the variable Notebook_file to reference the .dat

outputStr = "" #set as global in functions -> used for output log


#Creates a custom exception class called ExitNotFoundError and initializes its parameters
class ExitNotFoundError(Exception):
    def __init__(self,location_name,message ='INSERT ERROR MESSAGE HERE'):
        self.location_name = location_name
        self.message = message

    #defines the function that displays the error message
    def __str__(self):
        return f"{self.location_name} -> {self.message}"

#creates the Notebook class for reading and access the player's notes throughout the game
class Notebook:
    def __init__(self, notebook_file):
        self.notebook_file = notebook_file

    def write_entry(self, entry): #writing -> uses append so won't overwrite 
        with open(self.notebook_file, 'a') as f:
            f.write(entry + '\n')

    def read_entries(self): #for just reading the notebook file
        try:
            with open(self.notebook_file, 'r') as f:
                entries = f.readlines()
                if not entries:
                    str = "Notebook is empty.\n"
                    outputStr += str
                    print(str)
                else:
                    print("Entries in Notebook:")
                    for entry in entries:
                        print(entry.strip())
        except FileNotFoundError:
            print("Notebook file not found.")

#Creates a class named Locations and initializes its parameters
class Locations:
    def __init__(self,name,description,exits):
        self.name = name
        self.description = description
        self.exits = exits

    #defines function that returns name of the location
    def get_name(self):
        return self.name

    #defines function that returns the matching description of the respective location
    def get_description(self):
        return self.description

    #defines function that returns the exits
    def get_exits(self):
        return self.exits

    #defines function that returns the exits in the form of a list
    def list_exits(self):
        return "\n".join(self.exits)

    #defines function that returns the name, description, and exits in order
    def __str__(self):
        return f"{self.name}: {self.description}\n\nExits:\n{self.list_exits()}"

#Creates a class named GameMap and initializes its parameter
class GameMap:
    def __init__(self):
        self.map = {}

    #defines function that adds the location and location name to the dictionary
    def add_location(self,location):
        self.map[location.get_name().lower()] = location

    #defines function that determines if the entered error is correct and raises the error if not
    def get_location(self,location_name):
        location = self.map.get(location_name.lower())
        if location is None:
            raise ExitNotFoundError(location_name)
        return location

def main(): 
    #Intro Title Sequence
    print()
    print('      Silent Suburbia      ')
    print('___________________________')
    print()
    print('  Written and Developed by ')
    print('   Aidan Graves, 4/16/24   ')
    print()
    print()
    print()
    print('Enter "N" to Start a New Game')
    print('Enter "L" to Load a Saved Game')

    user_input = input().upper()

    while user_input not in ["N", "L"]:
        print('Enter "N" to Start a New Game or "L" to Load a Saved Game')
        user_input = input().upper()

    #game = Game()

    if user_input == "N":
        pass
        #game.start_new_game()
    elif user_input == "L":
        pass
        #game.load_game()

    #creates an instance of the GameMap class named game_map
    game_map = GameMap()
    
    #creates an instance of the NoteBook class named notebook
    notebook = Notebook(Notebook_file)

    #makes a title to the notebook at the start of every game.
    notebook_entry1 = 'This is the Notebook of Nathaniel Damascus Brooks:\n'
    notebook.write_entry(notebook_entry1)

    #assigns each location with their respective description
    game_map.add_location(Locations("Outside", "INSERT DESCRIPTION", ['Family Room']))
    game_map.add_location(Locations("Family Room", "INSERT DESCRIPTION", ["Holodeck", "Trophy Locations", "Study"]))
    game_map.add_location(Locations("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Locations"]))
    game_map.add_location(Locations("Study", "Do you love being disturbed while working? This location has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Outside", "Library", "Bedroom"]))
    game_map.add_location(Locations("Holodeck", "A location that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"]))
    game_map.add_location(Locations("Trophy Locations", "Spacious location with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"]))
    game_map.add_location(Locations("Bedroom", "A lavished bed adorns the center of this location, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom.", ["Study", "Trophy Locations"]))

    #sets current_room to the starter location, being the study
    current_room = game_map.get_location("Outside")

    #initializes bool_to_not_print_entire_thing
    bool_to_not_print_entire_thing = True

    #runs until a break happens
    while True:
        #checks that bool_to_not_print_entire_thing is true to print the updated current location
        if bool_to_not_print_entire_thing == True:
            print(current_room)
        #re-initializes bool_to_not_print_entire_thing
        bool_to_not_print_entire_thing = True
        print("Please choose an exit: ")
        exit_choice = input().strip().lower()

        # try statement containing whether or not the code remains to run, breaks, or has an error
        try:
            if exit_choice == "exit":
                print("Exiting the house out of the nearest window... thanks for the tour!")
                break

            elif exit_choice == "write notes": # if player wants to write in notebook
                notebook_entry = input("Write something in your notebook: ")
                notebook.write_entry(notebook_entry)
                print("Entry added to notebook.")
                continue  # Skip the rest of the loop iteration

            elif exit_choice == "read notes": # if player wants to read notebook
                notebook.read_entries()
                continue  # Skip the rest of the loop iteration

            elif exit_choice not in map(str.lower, current_room.get_exits()):
                raise ExitNotFoundError(exit_choice)
            else:
                current_room = game_map.get_location(exit_choice)

        except ExitNotFoundError as e:
            print(e)
            bool_to_not_print_entire_thing = False
            
#runs main
if __name__ == "__main__":
    main()




'''
Main text of the game -> to be put in once the actual coding works

print("The sun hung low in the sky, casting long shadows across the manicured 
lawns of Elmwood Estates. I parked my government-issued sedan at the curb, the 
engine’s hum a stark contrast to the silence that enveloped the neighborhood. 
Just hours before, the shrill screams and laughter of children playing rang in
the entire neighborhood. Now, all was still, as if waiting eagerly for something,
anything, to happen. 

Next to my torn-up, cheap leather notebook was the weapon I was burdened with
carrying: The clipboard. It rested on the passenger seat holding the eviction 
notice, its crisp edges a reminder of my purpose here. It's not a fun job; 
no one ever grows up excited to do this, but someone had to. It pays the bills,
supports the family, well... future family, that is. Plus no one likes their job,
right? It's a means to an end. It puts the food on my plate, gas in my car, and
occassional beer in my hand. Yep, livin' the dream.

I stepped out, adjusting my thin argyle tie, and surveyed the house before me. 
Number 42 Maplewood Drive. A typical suburban abode, complete with a white 
picket fence, blooming azaleas, white toyota camry in the driveway, and a 
rusting swing set in the backyard. 
The curtains twitched in the window, revealing a glimpse of life inside, 
before immediately being still. 'That can't be right', I muttered to myself.
This was supposed to be a quick one. No one had seen or heard from the resident
in over a month, they had dissappeared.")
'''