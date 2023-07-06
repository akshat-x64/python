class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name:{self.name}")
        print(f"species:{self.species}")


class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog")
        self.breed = breed

    def show_details(self):
        animal.show_details(self)
        print(f"breed: {self.breed}")


class goldanRetriever(dog):
    def __init__(self, name, color):
        dog.__init__(self, name, breed="goldanRetriever")
        self.color = color

    def show_details(self):
        dog.show_details(self)
        print(f"color: {self.color}")


o = goldanRetriever("Tommy", "golden")
o.show_details()
