import sys
from CowLab.heifer_generator import get_cows


def list_cows(cows):
    # display available cows
    # want to print out their name not the cow objects
    print("Cows available: ", " ".join([cow.get_name() for cow in cows]))


def find_cow(name, cows):
    # loop over our cows and want to kno if cow-get)name is equal to our name here then we return name 
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


def main():
    cows = get_cows()
    if sys.argv[1] == "-l":
        list_cows(cows)
    elif sys.argv[1] == "-n":
        print("Print message for", sys.argv[2])
        found_cow = find_cow(sys.argv[2], cows)
        if found_cow is None:
            print(f"Could not find {sys.argv[2]} cow!")
    else:
        print("found_cow.get_image()")

if __name__ == "__main__":
    main()