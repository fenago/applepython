class Animals:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.diet = None
        self.habitat = None
        self.species = None

    def set_diet(self, diet):
        self.diet = diet

    def set_habitat(self, habitat):
        self.habitat = habitat

    def set_species(self, species):
        self.species = species

    def calculate_food_consumption(self):
        return self.weight * 0.025

    def display_info(self):
        food_consumption = self.calculate_food_consumption()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Diet: {self.diet}")
        print(f"Habitat: {self.habitat}")
        print(f"Species: {self.species}")
        print(f"Food consumption: {food_consumption}")

class Mammals(Animals):
    def __init__(self, name, age, weight, legs, fur):
        super().__init__(name, age, weight)
        self.legs = legs
        self.fur = fur

    def display_info(self):
        super().display_info()
        print(f"Legs: {self.legs}")
        print(f"Fur: {self.fur}")
lion = Mammals("Simba", 5, 200, 4, "Golden")
lion.set_diet("Carnivore")
lion.set_habitat("Savanna")
lion.set_species("Panthera leo")
lion.display_info()
