print("Hello world")

#pet dictionary
pet_1 = {"animal": "dog",
         "owner": "sam"}

pet_2 = {"animal": "cat",
         "owner": "samuel"}

#all pets in a list
pets = [pet_1, pet_2]

#print
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")