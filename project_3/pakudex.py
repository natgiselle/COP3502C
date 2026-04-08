from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.pakuri_list:
            return None
        species_array = []

        for p in self.pakuri_list:
            species_array.append(p.get_species())
        return species_array

    def get_stats(self, species):
        for p in self.pakuri_list:
            if p.get_species() == species:
                return [p.get_attack(), p.get_defense(), p.get_speed()]
        return None

    def sort_pakuri(self):
        # the sort() method also works on strings so it extracts the names, sorts them, rebuilding the list matching that order
        species_names = []
        for p in self.pakuri_list:
            species_names.append(p.get_species())
        species_names.sort()

        sorted_list = []
        for name in species_names:
            for p in self.pakuri_list:
                if p.get_species() == name:
                    sorted_list.append(p)
                    break
        self.pakuri_list = sorted_list

    def add_pakuri(self, species):
        if len(self.pakuri_list) >= self.capacity:
            return False
        for p in self.pakuri_list:
            if p.get_species() == species:
                return False
        self.pakuri_list.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        for p in self.pakuri_list:
            if p.get_species() == species:
                p.evolve()
                return True
        return False