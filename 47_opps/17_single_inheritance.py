class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("This sound is made by an animal")


class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("This sound is made by an dog")


a1 = animal("cow", "carnivorous")
a1.make_sound()

a2 = dog("dog", "dog")
a2.make_sound()
print(a2)
print(a2.name, a2.species, a2.breed)


class cat(animal):
    def sing_song(self):
        print("Meo Meo")


catt = cat("aa", "b")
catt.sing_song()
