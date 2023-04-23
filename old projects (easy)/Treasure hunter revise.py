import sys
def main():
    print("Welcome to Ravenhold Castle Annual Treasure Hunt!")
    current_room = 1
    #This will let you append the item into the [] so the game can track if it been obtain.
    inventory = []
    #this is to set a condition for hidden events.
    search_count = 0 

    while True:
        print(f"You are in room {current_room}.")
        print(room_description(current_room))
        action = input("What would you like to do? (move/search/help/quit): \n").lower()

        if action == "move":
            current_room = move(current_room)
        elif action == "search":
            search_count, inventory = search(current_room, search_count, inventory)
        elif action == "help":
            display_help()
        elif action == "quit":
            print("You have fail.")
            sys.exit()
        else:
            print("Invalid action. Please try again.")

#this define the function for the room description and the room number
def room_description(room_number):
    descriptions = {
        #number is the room number
        1: "This is the entrance hall. There is a large door to the right.",
        2: "This is a dimly lit room with a bookshelf and a mysterious painting on the wall.",
        3: "This is a cozy room with a fireplace and a comfortable armchair.",
        4: "This is a dining room with a long table and several chairs.",
        5: "This is the kitchen. There are various cooking utensils and ingredients.",
        6: "This is a storage room filled with boxes and old furniture.",
        7: "This is a bedroom with a large bed and a wardrobe.",
        8: "This is a study room with a desk, a chair, and a bookshelf.",
        9: "This is a bathroom with a bathtub, a sink, and a mirror.",
        10: "This is a locked door. You need a key to open it."
    }
    return descriptions[room_number]

#This def the action user can take
def move(current_room):
    direction = input("Which way you like to go? (left/right). \n").lower()

    if direction == "left":
        current_room -= 1
    elif direction == "right":
        current_room += 1
    else:
        print("Invalid direction.")
        return current_room
    
    if current_room < 1:
        print("You cannot go any further. ")
        current_room = 1
    elif current_room >= 10:
        print("You have reach the lowest floor. ")
        current_room = 10

    return current_room
def search(current_room, search_count, inventory):
    search_count += 1

    if current_room == 2 and search_count > 1 and "knife" not in inventory:
        print("You found a rusty knife! Let grab it just in case. ")
        inventory.append("knife")
    elif current_room == 3 and search_count >= 2 and "key" not in inventory:
        print("You found an old key underneath the comfy chair!")
        inventory.append("key")
    elif current_room == 8 and search_count > 1 and "clue" not in inventory:
        print("You found a clue! In a Cozy room with a Comfortable chair there hidden the treasure you seek.")
        inventory.append("clues")
    elif current_room == 6 and search_count >= 5 and "knife" in inventory:
        print("You found a crack on the wall, the rusty knife was able to pry it open.")
        print("You found the hidden passage!")
        print("Congratulation you found the treasure!")
        sys.exit()
    elif current_room == 10 and "key" in inventory:
        print("Congratulation you found the Treasure room!!")
        print("Thank you for playing")
        sys.exit()
    elif current_room == 10 and search_count >= 2:
        print("Your greed had blind you.")
        print("You trigger a trap and the room fill with gas and kill you")
        print("game over!")
        sys.exit()
    else:
        print("There nothing here.")
    
    return search_count, inventory

def display_help():
    print("\mCommand: ")
    print(" move: Move to the next room (left/right)")
    print(" search: Search the current room for items and hidden clues.")
    print(" help: Display this help message")
    print(" quit: Quit the game aka loser!")

if __name__ == "__main__":
    main()
    