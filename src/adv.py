from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. There is are Skulls on the floor."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. You see a folded 
sheet of paper nearby."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been nearly completely emptied by
earlier adventurers. Something shines in the corner! The only exit is to the south."""),
}

#Declare initial items
Skull = Item("Skull", "A grey skull of average size. Probably belongs to a fallen adventurer.")
Gold = Item("Gold", "Some rare and valuable treasure.")
Treasure_Hint = Item("Map", "According to this map, the treasure lies to the north of a narrow passage.")


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Fill rooms with items
room['foyer'].room_inv.append(Skull)
room['overlook'].room_inv.append(Treasure_Hint)
room['treasure'].room_inv.append(Gold)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(location=room['outside'])
# Write a loop that:
#
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(player.location)
# * Waits for user input and decides what to do.
#
    command = input("Enter a Command> ").split(',')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    if command[0] == 'q':
        break

    elif command[0] == 'h':
        print(" ""q"" to quit. n to move north. s to move south. w to move west. e to move east.\n p [item name] to pick up items, d to drop them.")
    elif command[0] == 'n':
    #     # check if the player can move in the desired direction
        if player.location == room['outside'] or player.location == room['foyer'] or player.location == room['narrow']:
        #     # if player can move, set the room located in that direction as the players location
            player.location = player.location.n_to
            # if it's a dead end, let the player know
        else:
            print("DEAD END")

    elif command[0] == 's':
    #     # check if the player can move in the desired direction
        if player.location == room['foyer'] or player.location == room['overlook'] or player.location == room['treasure']:
        #     # if player can move, set the room located in that direction as the players location
            player.location = player.location.s_to
            # if it's a dead end, let the player know
        else:
            print("DEAD END")

    elif command[0] == 'e':
            #     # check if the player can move in the desired direction
        if player.location == room['foyer']:
        #     # if player can move, set the room located in that direction as the players location
            player.location = player.location.e_to
            # if it's a dead end, let the player know
        else:
            print("DEAD END")

    elif command[0] == 'w':
            #     # check if the player can move in the desired direction
        if player.location == room['narrow']:
        #     # if player can move, set the room located in that direction as the players location
            player.location = player.location.w_to
            # if it's a dead end, let the player know
        else:
            print("DEAD END")

    elif command[0] == "p":
        player.item_pickup(player.location.room_inv[0])
        print(f"You've picked up {player.inventory[0].print_item_name}!")


    else:
        print(f"ERROR:{command[0]} not valid. For a list of valid commands, enter ""h"". Try Again! ")