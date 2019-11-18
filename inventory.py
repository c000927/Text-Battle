# Charlie Sun
# CS 30
# Period 4
# November 15, 2019
# Inventory of the game


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


# Loop in the nested dictionary and print the info out
# item = 1st layer key, des = 2nd layer key
def print_inventory(inventory):
    for item, des in inventory.items():
        print("\n\nThe name of the item is: " + item)
        print(item + " is " + str(des["Description"]) + ".")
        print(item + " has " + str(des["HP Bonus"]) + " HP Bonus.")
        print(item + " has " + str(des["Probability"]*100) + "% probablity.")
