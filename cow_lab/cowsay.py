import sys
from heifer_generator import get_cows


def list_cows(cows):
    cow_names = []
    for cow in cows:
        cow_names.append(cow.get_name())
    print(f"Cows available: {' '.join(cow_names)}")


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


def main():
    cows = get_cows()

    if len(sys.argv) == 1:
        pass
    elif "-l" in sys.argv:
        list_cows(cows)
    elif "-n" in sys.argv:
        n_index = sys.argv.index("-n")
        cow_name = sys.argv[n_index + 1]
        message_parts = sys.argv[1:n_index]
        message = " ".join(message_parts)
        cow = find_cow(cow_name, cows)
        if cow is None:
            print(f"Could not find {cow_name} cow!")
        else:
            print(message)
            print(cow.get_image(), end="")
    else:
        message = " ".join(sys.argv[1:])
        cow = find_cow("heifer", cows)
        print(message)
        print(cow.get_image(), end="")


if __name__ == "__main__":
    main()