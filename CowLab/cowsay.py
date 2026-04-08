import sys
from heifer_generator import get_cows
from dragon import Dragon


def list_cows(cows):
    print("Cows available: " + " ".join([cow.get_name() for cow in cows]))


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


def main():
    cows = get_cows()
    if sys.argv[1] == "-l":
        list_cows(cows)
    elif sys.argv[1] == "-n":
        found_cow = find_cow(sys.argv[2], cows)
        if found_cow is None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            print(" ".join(sys.argv[3:]))
            print(found_cow.get_image())
            if isinstance(found_cow, Dragon):
                if found_cow.can_breath_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
    else:
        found_cow = find_cow("heifer", cows)
        print(" ".join(sys.argv[1:]))
        print(found_cow.get_image())

if __name__ == "__main__":
    main()