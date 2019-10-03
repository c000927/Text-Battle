# Charlie Sun
# CS 30
# Period 4
# September 27, 2019
# Print the inventory of the RPG game in the lists

# Create a list of weapons and append items to it
weapons = []
weapons.append("M9")
weapons.append("M1014")
weapons.append("M4A1 SOPMOD")
weapons.append("HK416")
weapons.append("MP5A3")
weapons.append("M249 SAW")
weapons.append("Mark 12 Mod 0 SPR")
weapons.append("M24A2 SWS")
weapons.append("MK 14 Mod 0 EBR")
weapons.append("M107")

# Create a list of medicaiton and append items to it
medication = []
medication.append("Bandage")
medication.append("First Aid Kit")
medication.append("Med Kit")
medication.append("Energy Drink")
medication.append("Painkillers")


# Create a function to print the lists
def printLists(title_name, list_name):
    print("Available " + title_name + ":")  # Print the title of list
    counter = 0  # Set thee counter to 0
    for list_item in list_name:  # Create a loop to access the items in list
        counter += 1  # Add 1 to counter everytime
        print(str(counter) + ". " + list_item)  # Print the message


printLists("weapons", weapons)  # Print the weapons list
printLists("medication", medication)  # Print the medication list
