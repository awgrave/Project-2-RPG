''' 
Aidan Graves
4/16/24
CPSC 1050 Project 2 - RPG

CODE DESCRIPTION:
This is the 2nd project for CPSC 1050. The assignment is to create a RPG video game. My video game is a text based mystery game about 
a disturbing disappearance in a seemingly normal suburban home. 

GITHUB LINK: 
https://github.com/awgrave/Project-2-RPG
'''
##NOT USED:
#import pickle #used for saving game data and loading from save files
#import os #used for wiping saved data for new playthroughs
#Save_game_data = 'savegame.dat' #uses the variable Notebook_file to reference the .dat


#Instead of a Save and Load Game Feature, using an output log
output_log_file = 'output_log.txt' #sets variable for save log feature

Notebook_file = 'Notebook.txt' #uses the variable Notebook_file to reference the .txt

#functions to make sure output log and notebook are empty at the start of the game:
# Function to clear the notebook file
def clear_notebook():
    with open(Notebook_file, 'w') as f:
        f.write('')

# Function to clear the output log file
def clear_output_log():
    with open(output_log_file, 'w') as f:
        f.write('')

# function to append all of the output text to the output log file
def append_to_log(text):
    with open(output_log_file, 'a') as log_file:
        log_file.write(text + '\n')

#Creates a custom exception class called ErrorMessage and initializes its parameters
class ErrorMessage(Exception):
    def __init__(self, message ="Invalid input. Please enter 'Yes', 'No', 'Write notes', or 'Read notes'."):
        self.message = message
        append_to_log(message)

    #defines the function that displays the error message
    def __str__(self):
        return self.message

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
                    print("Notebook is empty.")
                    append_to_log("Notebook is empty.")
                else:
                    print("Entries in Notebook:")
                    append_to_log("Entries in Notebook:")
                    for entry in entries:
                        print(entry.strip())
                        append_to_log(entry.strip())

        except FileNotFoundError:
            print("Notebook file not found.")
            append_to_log("Notebook file not found.")

#Creates a class named Locations and initializes its parameters
class Locations:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    #defines function that returns name of the location
    def get_name(self):
        return self.name

    #defines function that returns the matching description of the respective location
    def get_description(self):
        return self.description

    #defines function that returns the name, description, and exits in order
    def __str__(self):
        return f"{self.name}: {self.description}"

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
            raise ErrorMessage(location_name)
        return location


def main(): 
    ### SECTION 0
    # Clear the notebook and output log files
    clear_notebook()
    clear_output_log()
    
    # Intro Title Sequence
    print()
    print('       Silent Suburbia     ')
    print('___________________________')
    print()
    print('  Written and Developed by ')
    print('    Aidan Graves, 4/16/24  ')
    print()
    print()
    print()
    print('   Enter any key to begin  ')
    
    append_to_log('Silent Suburbia')
    append_to_log('Written and Developed by Aidan Graves, 4/16/24')
    append_to_log('Enter any key to begin')

    user_input = input().upper()

    # creates an instance of the GameMap class named game_map
    game_map = GameMap()
    
    # creates an instance of the NoteBook class named notebook
    notebook = Notebook(Notebook_file)

    # makes a title to the notebook at the start of every game.
    notebook_entry_for_intro = 'This is the Notebook of Nathaniel Damascus Brooks:\n'
    notebook.write_entry(notebook_entry_for_intro)

    # assigns each location with their respective description - will be fully utilized past the Beta stage
    game_map.add_location(Locations("Outside", "INSERT DESCRIPTION"))
    game_map.add_location(Locations("Family Room", "INSERT DESCRIPTION"))
    game_map.add_location(Locations("Kitchen", "INSERT DESCRIPTION"))
    game_map.add_location(Locations("Bathroom,", "INSERT DESCRIPTION",))
    game_map.add_location(Locations("Basement", "INSERT DESCRIPTION"))
    game_map.add_location(Locations("Bedroom", "INSERT DESCRIPTION"))

    # sets current_room to the starter location, being the Bathroom,
    current_room = game_map.get_location("Outside")

    ### SECTION 1
    #Starting text of the game
    # Putting block of text in the output_log
    Outside_text = """
    The sun hung low in the sky, casting long shadows across the manicured
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
    rusting swing set in the backyard.The curtains twitched in the window, revealing 
    a glimpse of life inside, before immediately being still, as if it never happened.
    'That can't be right', I muttered to myself. This was supposed to be a quick one. 
    No one had seen or heard from the resident in over a month, they had dissappeared.

    Now I don't spook easily, but... was there really someone there? I blinked twice
    and rubbed my eyes in an attempt to shake off the sleep deprivation. And then
    it hit me. Duh, it was probably just squatters. Those scum of the earth nuisances
    will bury themselves in anything with a roof. Now I've also dealt with enough 
    squatters to know that guns are very easy to get your hands on these days. 
    And I need to be alive to be paid. I'd best just call the cops and have them
    deal with it. But still, something in the back of my mind couldn't help but think
    that that wasn't it either. 

    Glancing at my watch, I noticed that five minutes had already passed since parking.
    I had wasted enough time, I needed to be decisive. Should I ask the neighbors if
    they've heard anything recently?

    """

    print(Outside_text)
    # Appending to log
    append_to_log(Outside_text.strip())

    skip_neighbor_dialogue = False #Boolean for user choice

    # runs until a break happens
    while True: ## FIRST LOOP
        print("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
        append_to_log("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
        action_choice = input().strip().lower()

        # try statement containing whether or not the code remains to run, breaks, or has an error
        try:
            if action_choice == "exit the game":
                print("Exiting the game. Thanks for playing!")
                append_to_log("Exiting the game. Thanks for playing!")
                exit(1)

            elif action_choice == "use notebook":  # if player wants to use the notebook
                print("Would you like to 'write' or 'read' from your notebook?")
                append_to_log("Would you like to 'write' or 'read' from your notebook?")
                notebook_action = input().strip().lower()

                if notebook_action == "write":
                    print("Write something in your notebook: ")
                    append_to_log("Write something in your notebook: ")
                    notebook_entry = input().strip().lower()
                    notebook.write_entry(notebook_entry)
                    append_to_log(notebook_entry)
                    print("Entry added to notebook.")
                    append_to_log('Entry added to notebook.')

                elif notebook_action == "read":
                    notebook.read_entries()
                    
                else:
                    raise ErrorMessage("Invalid input. Please enter 'write' or 'read'.")
                continue  # Skip the rest of the loop
            
            elif action_choice == "yes":
                skip_neighbor_dialogue = False
                break  # Exit the loop

            elif action_choice == "no":
                skip_neighbor_dialogue = True
                break  # Exit the loop

            else:
                raise ErrorMessage("Invalid input. Please enter 'Yes', 'No', 'Write notes', or 'Read notes'.")
                
        except ErrorMessage as e:
            print(e)

    ### SECTION 2

    if skip_neighbor_dialogue:
        Outside_text_transition = '''
        No, I shouldn't bother them, the sun is starting to set anyways. A slight breeze picked up, sending a chill down my spine. 
        The curtains inside the house were still, but the air held a tension I couldn’t explain. I took a deep breath and knocked, 
        my knuckles rapping against the wood. No answer. Defeated, confused, and extremely tired,
        I was ready to give up. Should I?
        '''
        print(Outside_text_transition)
        append_to_log(Outside_text_transition)

    else: #if user wanted to ask the neighbors
        Neighbor_dialogue = '''
        I figured there was no harm in asking. I walked across the neatly trimmed lawn, my footsteps muffled by the dew. 
        The neighboring houses stood like silent sentinels, their windows lit by lamplight. I knocked on the door of House number 40, hoping for answers.
        There was no response. As I went to knock again, the lock started shifting and the door slowly swung open.
        An elderly woman peaked her head out, her eyes widening when she saw me, clipboard in hand. "May I help you?"
        she groaned, her voice a mix between gravel and a whisper, like nails on a chalkboard. “Have you heard anything from the house next door recently?
        Anything unusual?” She leaned in, her breath warm against my cheek. My head retracted back at the smell of her breath, physically revolting 
        at the soulless stench. “Haven’t seen a soul there in weeks,” she said. Reassured with her answer, I thanked her and started to turn away. 
        "Besides the crying" she whispered. I started to turn back around, convinced I misheard. "Excuse me ma'am, what..." before the door slammed shut.

        As I walked back to the house, my mind raced. Crying? In a vacant house? The hairs on my neck stood on end. There's two logical solutions here,
        I either misheard, or that old lady is crazy. Both were extremely possible, so I needed to stop worrying and start doing my job. But my
        stomach started to twist, my mind running through all the possibilities. I needed to investigate further. Perhaps the missing resident wasn’t 
        missing at all. Perhaps they were trapped, their cries echoing through the empty rooms. I glanced back at the neighboring house — their windows now dark, 
        as if they too held their breath.

        I returned back to Number 42 Maplewood Drive, my footsteps echoing louder this time. The curtains remained still, but the air held a tension 
        I couldn’t explain. I took a deep breath and knocked, my knuckles rapping against the wood. No answer. Defeated, confused, and extremely tired,
        I was ready to give up. Should I?
        '''

        print(Neighbor_dialogue)
        append_to_log(Neighbor_dialogue)


        # runs loop again
    while True:  # SECOND LOOP
        print("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
        append_to_log("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
        action_choice = input().strip().lower()

        # try statement containing whether or not the code remains to run, breaks, or has an error
        try:
            if action_choice == "exit the game":
                print("Exiting the game. Thanks for playing!")
                append_to_log("Exiting the game. Thanks for playing!")
                exit(1)

            elif action_choice == "use notebook":  # if player wants to use the notebook
                print("Would you like to 'write' or 'read' from your notebook?")
                append_to_log("Would you like to 'write' or 'read' from your notebook?")
                notebook_action = input().strip().lower()

                if notebook_action == "write":
                    print("Write something in your notebook: ")
                    append_to_log("Write something in your notebook: ")
                    notebook_entry = input().strip().lower()
                    notebook.write_entry(notebook_entry)
                    append_to_log(notebook_entry)
                    print("Entry added to notebook.")
                    append_to_log('Entry added to notebook.')

                elif notebook_action == "read":
                    notebook.read_entries()
                    
                else:
                    raise ErrorMessage("Invalid input. Please enter 'write' or 'read'.")
                continue  # Skip the rest of the loop
            
            elif action_choice == "no":
                while True:  # Nested loop for 'No' choice
                    print("I waited and knocked again, but still no response. It's getting late, I should probably give up. Should I?")
                    append_to_log("I waited and knocked again, but still no response. It's getting late, I should probably give up. Should I?")
                    print("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
                    append_to_log("Please choose an action: 'Yes', 'No', 'Use notebook', or 'Exit the game'")
                    inner_action_choice = input().strip().lower()
                    if inner_action_choice == 'no':
                        continue  # Continue the nested loop if the choice is 'no'
                    elif inner_action_choice == 'yes':
                        break  # Exit the nested loop if the choice is 'yes'
                    else:
                        raise ErrorMessage("Invalid input. Please enter 'Yes' or 'No'.")
                # Break out of the outer loop if the inner loop exits with 'yes'
                break
            
            elif action_choice == "yes":
                break  # Exit the main loop if the choice is 'Yes'

            else:
                raise ErrorMessage("Invalid input. Please enter 'Yes', 'No', 'Write notes', or 'Read notes'.")
                
        except ErrorMessage as e:
            print(e)


    ### SECTION 3
    finding_the_keys = '''
    I finally decided to give up and started walking back to my car. But just as I walked past the white sedan in the driveway,
    a glimmer of light caught my eye. The street lamp’s glow reflected off a pair of keys sitting on the car’s dash. They looked 
    ordinary — just a simple keychain with a worn-out leather tag, the car key, and another, regular key. I hesitated. Surely not… 
    but curiosity gnawed at me. The house behind me held secrets, and those keys might unlock them. My hand trembled as I reached for 
    the car door. And lo and behold, it swung open with ease, as if inviting me in. The interior smelled of stale air and old upholstery.
    I grabbed the keys off the dash and examined them in the light of the street lamp, the sun now hiding behind the mountain horizon.
    FINISH TEXT HERE
        
    '''
    print(finding_the_keys)
    append_to_log(finding_the_keys)

# runs main
if __name__ == "__main__":
    main()

