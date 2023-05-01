import sys

def main():
    print("Welcome to the Treasure Hunt!")
    current_room = 1
    inventory = []
    search_count = 0

    while True:
        print(f"\nYou are in room {current_room}.")
        print(room_description(current_room))
        action = input("What would you like to do? (move/search/help/quit): ").lower()

        if action == "move":
            current_room = move(current_room)
        elif action == "search":
            search_count, inventory = search(current_room, search_count, inventory)
        elif action == "help":
            display_help()
        elif action == "quit":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid action. Please try again.")

def room_description(room_number):
    descriptions = {
        1: "This is the entrance hall. There is a large door to the right.",
        2: "This is a dimly lit room with a bookshelf and a mysterious painting on the wall.",
        3: "This is a cozy room with a fireplace and a comfortable armchair.",
        4: "This is a dining room with a long table and several chairs.",
        5: "This is the kitchen. There are various cooking utensils and ingredients.",
        6: "This is a storage room filled with boxes and old furniture.",
        7: "This is a bedroom with a large bed and a wardrobe.",
        8: "This is a study room with a desk, a chair, and a bookshelf.",
        9: "This is a bathroom with a bathtub, a sink, and a mirror.",
        10: "This is a locked door leading to the treasure room. You need a key to open it."
    }
    return descriptions[room_number]

def move(current_room):
    direction = input("Which direction would you like to move? (left/right): ").lower()

    if direction == "left":
        current_room -= 1
    elif direction == "right":
        current_room += 1
    else:
        print("Invalid direction. Please try again.")
        return current_room

    if current_room < 1:
        print("You cannot go any further left.")
        current_room = 1
    elif current_room > 10:
        print("You cannot go any further right.")
        current_room = 10

    return current_room

def search(current_room, search_count, inventory):
    search_count += 1

    if current_room == 5 and "knife" not in inventory:
        print("You found a knife!")
        inventory.append("knife")
    elif current_room == 8 and "key" not in inventory:
        print("You found a key!")
        inventory.append("key")
    elif current_room == 3 and "clue" not in inventory:
        print("You found a clue! The key is hidden in a room with an even number.")
        inventory.append("clue")
    elif current_room == 10 and "key" in inventory:
        print("Congratulations! You found the treasure room and unlocked it with the key!")
        sys.exit()
    elif current_room == 2 and search_count >= 4 and "knife" in inventory:
        print("You discovered a hidden passage to the treasure room!")
        print("Congratulations! You found the treasure!")
        sys.exit()
    else:
        print("You found nothing.")

    return search_count, inventory

def display_help():
    print("\nCommands:")
    print("  move: Move to the next room (left or right).")
    print("  search: Search the current room for items or clues.")
    print("  help: Display this help message.")
    print("  quit: Quit the game.")

if __name__ == "__main__":
    main()