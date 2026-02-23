print("Hello world")

#pet dictionary
pet_1 = {"Animal": "Dog",
         "Owner": "Samuel"}

pet_2 = {"Animal": "Cat",
         "Owner": "Michael"}

pet_3 = {"Animal": "Parrot",
         "Owner": "Benjamin"}

pet_4 = {"Animal": "Hamster",
         "Owner": "John"}

#all pets in a list
pets = [pet_1, pet_2, pet_3, pet_4]

#print
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")