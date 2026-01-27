'''
Write a program called animals.py that guesses what animal something is based on a couple questions.
If it has legs and is fluffy, its a cat!
If it has legs and is not fluffy, its a gator!
If it does not have legs and lives on land, its a snake!
If it does not have legs and does not live on land, its a shark!
'''
has_legs = input("Does it have legs [y/n]: ")
if has_legs == "y":
    is_fluffy= input("Is it fluffy [y/n]: ")
    if is_fluffy == "y":
        print("It's a cat!")
    elif is_fluffy == "n":
        print("It's a gator!")
elif has_legs == "n":
    on_land = input("Does it live on land [y/n]: ")
    if on_land == "y":
        print("It's a snake!")
    elif on_land == "n":
        print("It's a shark!")
# on_land = input("Does it live on land [y/n]: ")
