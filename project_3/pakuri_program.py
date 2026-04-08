from pakudex import Pakudex

def print_menu():
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        raw = input("Enter max capacity of the Pakudex: ")
        try:
            capacity = int(raw)
            if capacity > 0:
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")
            
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    while True:
        print_menu()
        choice = input("\nWhat would you like to do? ")

        if choice == "1":
            species = pakudex.get_species_array()
            if species is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                i = 1
                for s in species:
                    print(f"{i}. {s}")
                    i += 1

        elif choice == "2":
            name = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(name)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                print(f"\nSpecies: {name}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")

        elif choice == "3":
            if pakudex.get_size() >= pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                name = input("Enter the name of the species to add: ")
                if pakudex.get_stats(name) is not None:
                    print("Error: Pakudex already contains this species!")
                else:
                    pakudex.add_pakuri(name)
                    print(f"Pakuri species {name} successfully added!")

        elif choice == "4":
            name = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(name):
                print(f"{name} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()