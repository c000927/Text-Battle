# Charlie Sun
# CS 30
# Period 4
# November 15, 2019
# Locations of the game


# Create the dictionary of locations with description
locations = {"ST": "the spawn of the player which is the start point.",
             "E1": "the 1st level enemy which is the weakest.",
             "E2": "the 2nd level enemy which is weak.",
             "E3": "the 3rd level enemy which is medium.",
             "E4": "the 4th level enemy which is intermediate.",
             "EM": "the empty lcoation.",
             "HQ": "the headquate of enemy which is your final destination."
             }


# Loop in thedictionary and print the info out
# location = keys
def print_locations(locations):
    for location in locations:
        print(location + " is " + locations[location])
