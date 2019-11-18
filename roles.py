# Charlie Sun
# CS 30
# Period 4
# November 15, 2019
# Roles of the game

# Create the dictionary of roles with description, AP, HP, Accuracy and weapon
roles = {"Assault":  # Create the role Assault
         {"Description": "Basic Role",
             "Attack Points": 90,
             "Health Points": 100,
             "Accuracy": 0.8,
             "Weapons": ["M4A1", "M9"]
          },
         "CQB":  # Create the role CQB
         {"Description": "Medium Range Specialist",
             "Attack Points": 30,
             "Health Points": 110,
             "Accuracy": 0.7,
             "Weapons": ["HK MP5", "HK45CT"]
          },
         "Demolition":  # Create the role Demolitoin
         {"Description": "Close Range Specialist",
             "Attack Points": 80,
             "Health Points": 110,
             "Accuracy": 0.5,
             "Weapons": ["M870", "P226"]
          },
         "Supporter":  # Create the role Supporter
         {"Description": "Fire Support Role",
             "Attack Points": 70,
             "Health Points": 70,
             "Accuracy": 0.65,
             "Weapons": ["M249 SAW", "Glock 17"]
          },
         "Sniper":  # Create the role Sniper
         {"Description": "Long Range Specialist",
             "Attack Points": 100,
             "Health Points": 40,
             "Accuracy": 0.85,
             "Weapons": ["MK 20 Mod 0 SSR", "M9"]
          }
         }


# Loop in the nested dictionary and print the info out
# roles = 1st layer key, char = 2nd layer key
def print_roles(roles):
    for role, char in roles.items():
        print("\n\nThe name of the role is: " + role)
        print(role + "'s description is " + str(char["Description"]) + ".")
        print(role + " has " + str(char["Attack Points"]) + " Attack Points.")
        print(role + " has " + str(char["Health Points"]) + " Heealth Points.")
        print(role + " has the accuracy of " + str(char["Accuracy"]*100) + "%")
        print(role + " has following weapons: ")
        for weapons in char["Weapons"]:
            print("    - " + weapons)
