class Vet:
    animals = []
    space = 5

    def __init__(self, vet_name):
        self.vet_name = vet_name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space == len(Vet.animals):
            return "Not enough space"

        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"



    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        Vet.animals.remove(animal_name)
        self.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"


    def info(self):
        return f"{self.vet_name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"



peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())























