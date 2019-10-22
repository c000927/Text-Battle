# Charlie Sun
# CS 30
# Period 4
# October 21, 2019
# Make the RPG Nested Dictionaries with game info

# Create the dictionary of roles with description, AP, HP, Accuracy and weapon
roles = {"Assault": # Create the role Assault
            {"Description": "Basic Role",
             "Attack Points": 90,
             "Health Points": 100,
             "Accuracy": 0.8,
             "Weapons": ["M4A1", "M9"]
            },
         "CQB": # Create the role CQB
            {"Description": "Medium Range Specialist",
             "Attack Points": 30,
             "Health Points": 110,
             "Accuracy": 0.7,
             "Weapons": ["HK MP5", "HK45CT"]
            },
         "Demolition": # Create the role Demolitoin
            {"Description": "Close Range Specialist",
             "Attack Points": 80,
             "Health Points": 110,
             "Accuracy": 0.5,
             "Weapons": ["M870", "P226"]
            },
         "Supporter": # Create the role Supporter
            {"Description": "Fire Support Role",
             "Attack Points": 70,
             "Health Points": 70,
             "Accuracy": 0.65,
             "Weapons": ["M249 SAW", "Glock 17"]
            },
         "Sniper": # Create the role Sniper
            {"Description": "Long Range Specialist",
             "Attack Points": 100,
             "Health Points": 40,
             "Accuracy": 0.85,
             "Weapons": ["MK 20 Mod 0 SSR", "M9"]
            }
        }

# Loop in the nested dictionary and print the info out
# roles = 1st layer key, char = 2nd layer key
for roles, char in roles.items():
    print("\n\nThe name of the role is: " + roles)
    print(roles + "'s description is " + str(char["Description"]) + ".")
    print(roles + " has " + str(char["Attack Points"]) + " Attack Points.")
    print(roles + " has " + str(char["Health Points"]) + " Heealth Points.")
    print(roles + " has the accuracy of " + str(char["Accuracy"]*100) + "%")
    print(roles + " has following weapons: ")
    for weapons in char["Weapons"]:
        print("    - " + weapons)

# Create the dictionary of locations with description
locations = {"ST": "the spawn of the player which is the start point.",
             "E1": "the 1st level enemy which is the weakest.",
             "E2": "the 2nd level enemy which is weak.",
             "E3": "the 3rd level enemy which is medium.",
             "E4": "the 4th level enemy which is intermediate.",
             "E5": "the 5th level enmey which is strong.",
             "E6": "the 6th level enemy which is strongest.",
             "HQ": "the headquate of enemy which is your final destination."
            }

# Print the line
print("\n\n" + "- - - - - - - - - - - -" + "\n\n")

# Loop in thedictionary and print the info out
# location = keys
for location in locations:
    print(location + " is " + locations[location])

# Create the dictionary of the meds with description, HP Bonus and Probability
inventory = {"Bandage":
                {"Description": "Basic Med",
                 "HP Bonus": 10,
                 "Probability": 0.3
                },
             "Energy Drink":
                {"Description": "Good Med",
                 "HP Bonus": 15,
                 "Probability": 0.25
                },
             "First Aid Kit":
                {"Description": "Intermediat Med",
                 "HP Bonus": 25,
                 "Probability": 0.2
                },
             "Painkillers":
                {"Description": "Nice Med",
                 "HP Bonus": 35,
                 "Probability": 0.15
                },
             "Med Kit":
                {"Description": "Best Med",
                 "HP Bonus": 50,
                 "Probability": 0.1
                }
            }

# Print the line
print("\n\n" + "- - - - - - - - - - - -" + "\n\n")

# Loop in the nested dictionary and print the info out
# item = 1st layer key, des = 2nd layer key
for item, des in inventory.items():
    print("\n\nThe name of the item is: " + item)
    print(item + " is " + str(des["Description"]) + ".")
    print(item + " has " + str(des["HP Bonus"]) + " HP Bonus.")
    print(item + " has " + str(des["Probability"]*100) + "% probablity.")
