''' 
Aidan Graves
4/16/24
CPSC 1050 Project 2 - RPG
'''
'''
#Saving and Loading Code
import pickle

# Function to save the game state to a file
def save_game(player_data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(player_data, f)

# Function to load the game state from a file
def load_game(filename):
    with open(filename, 'rb') as f:
        player_data = pickle.load(f)
    return player_data

# Example usage
player_data = {
    'name': 'Player1',
    'health': 100,
    'score': 500,
    # Add more game state data as needed
}

# Save the game
save_game(player_data, 'savegame.dat')
print("Game saved.")

# Load the game
loaded_data = load_game('savegame.dat')
print("Game loaded:")
print(loaded_data)

'''
'''
#Inventory Code:
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return True
        return False

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")

# Example usage
sword = Item("Sword", "A sharp blade for battle.")
potion = Item("Potion", "Restores health.")

inventory = Inventory()
inventory.add_item(sword)
inventory.add_item(potion)

inventory.display_inventory()

# Player uses potion
inventory.remove_item("Potion")

inventory.display_inventory()

'''






import pickle #used for saving game data and loading from save files
import os #used for wiping saved data for new playthroughs

Notebook_file = 'Notebook.txt' #uses the variable Notebook_file to reference the .txt
Save_game_data = 'savegame.dat' #uses the variable Notebook_file to reference the .dat

class Game:
    def __init__(self):
        self.player = Player()
        self.map = Map()
        self.notebook = Notebook(Notebook_file)

    def start_new_game(self):
        print("Starting a new game...")
        self.clear_saved_data()
        self.player.choose_location()

    def clear_saved_data(self):
        # Clears saved game data
        try:
            os.remove(Save_game_data)
        except FileNotFoundError:
            pass

        # Clears the notebook file
        try:
            os.remove(Notebook_file)
        except FileNotFoundError:
            pass

        # opens fresh notebook
        self.notebook = Notebook(Notebook_file)

    def start(self):
        self.play()

    def play(self):
        pass
        #while True:
            #self.player.display_location()
            #self.player.interact_with_location()
            
    def save_game(self):
        game_data = {
            'player': self.player,
            'map': self.map,
            'notebook_notes': self.notebook.notes,
        }
        with open(Save_game_data, "wb") as f:
            pickle.dump(game_data, f)
        print("Game saved.")

    def load_game(self):
        try:
            with open(Save_game_data, "rb") as f:
                game_data = pickle.load(f)
            self.player = game_data['player']
            self.map = game_data['map']
            self.notebook.notes = game_data['notebook_notes']
            print("Game loaded.")
        except FileNotFoundError:
            print("No saved game found.")

class Player:
    def __init__(self):
        self.name = "Nathan Brooks"
        self.location = "Outside the House"

    def display_location(self):
        print(f"You are currently {self.location}.")

    def interact_with_location(self):
        # Logic for interacting with the current location
        pass

    def perform_action(self, action):
        # Logic for performing different actions
        pass

    def display_help(self):
        # Display available actions or help information
        pass

class Map:
    def __init__(self):
        # Initialize map data
        pass

    # Methods for map creation, loading, etc.

class Notebook:
    def __init__(self, file_path):
        self.file_path = Notebook_file
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                self.notes = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # If the file doesn't exist, the notebook will start with no notes
            pass

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(self.notes))

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def display_notes(self):
        if not self.notes:
            print("Notebook is empty.")
        else:
            print("Notebook Notes:")
            for index, note in enumerate(self.notes, start=1):
                print(f"{index}. {note}")

def main(): 

    print('      Silent Suburbia      ')
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

    game = Game()

    if user_input == "N":
        game.start_new_game()
    elif user_input == "L":
        game.load_game()

    game.play()

if __name__ == "__main__":
    main()
