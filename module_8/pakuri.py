class Pakuri:  # class names don't require capitalization, but convention is PascalCase
    def __init__(self, name): # constructor doesnt need to return anything just initializes attributes
        self.name = name # creates an instance of the name attribute

    def attack(self, attack_name):
        pakuri_name = self.name # can just use self.name as well either works
        print(f"{pakuri_name} used {attack_name}!")

    def speak(self):
        print(f"{self.name}, {self.name}!")

pikabu = Pakuri("Pikabu")
pikabu.speak() # doesnt need any input as it only has self as the input
pikabu.attack("thunderbolt") # needs input because it involves more than just self so it requires only one input since its attack_name
