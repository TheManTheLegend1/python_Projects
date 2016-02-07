# Heros Inventory 2.0
# Demonstrates tuples

# create a tuple with some items and diplay with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing portion")
print("Your items:")
for item in inventory:
    print(item)

raw_input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have"), len(inventory), ("items in your possession.")

raw_input("\nPress enter key to continue.")

# Test for membership with in
if "healing postion" in inventory:
    print("You will live to fight another day.")

# Display one item through an index
index = int(raw_input("\nEnter the index number for an item in inventory: "))
print"At index", index, "is", inventory[index]

# display a slice
start = int(raw_input("\nEnter the index number to begin a slice: "))
finish = int(raw_input("Enter the index number to end the slice: "))
print"inventory[", start, ":", finish, "] is"
print inventory[start:finish]

raw_input("\nPress the enter key to continue.")

# concatenate two tuples
chest = ("gold", "gems")
print"You find a chest.  It contains:"
print chest
print "You add the contents of the chest to you inventory."
inventory += chest
print "Your inventory is now: "
print inventory

raw_input("\n\nPress the enter key to exit.")
