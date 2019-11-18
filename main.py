# Charlie Sun
# CS 30
# Period 4
# November 15, 2019
# Create a map for the game

# Import modules and libraries
import menu
import roles
import locations
import inventory
from tabulate import tabulate

# The map of the game
map = [["ST", "EM", "EM", "E1", "EM"],
       ["EM", "EM", "E2", "EM", "EM"],
       ["E3", "EM", "E3", "EM", "E3"],
       ["EM", "E4", "HQ", "E4", "EM"]]

# Print the map as a grid
print(tabulate(map, tablefmt="grid"))

# Print a line
print("\n- - - - - - - - - - - - - - - - - - - - - - - -\n")

# Call the roles printer screen function
roles.print_roles(roles.roles)

# Print a line
print("\n- - - - - - - - - - - - - - - - - - - - - - - -\n")

# Call the inventory printer screen function
inventory.print_inventory(inventory.inventory)

# Print a line
print("\n- - - - - - - - - - - - - - - - - - - - - - - -\n")

# Call the locations printer screen function
locations.print_locations(locations.locations)

# Print a line
print("\n- - - - - - - - - - - - - - - - - - - - - - - -\n")

# Call the main title screen function
menu.title_screen()
