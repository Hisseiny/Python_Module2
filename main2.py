
print("------------------------ Exercice 1 -----------------------------------")
# TODO: Create a list of your favorite fruits
fruits = ["Orange", "Mango", "grapes"]

print("list of my fav fruits: ", )

# TODO: Add a new fruit to the end of the list
print("adding new fruit :) : ", fruits.append("Banana"))


# TODO: Remove the second fruit from the list

print("removing orange :( with pop ", fruits.pop(1))


# TODO: Sort the list alphabetically

print("Sorting my list :", fruits.sort())
# TODO: Create a new list with the first three fruits
newFruits = ["Orange", "Mango", "grapes"]

# Print the original list and the new list

print("Nouveau List ", newFruits)

print("------------------------ Exercice 2 -----------------------------------")
# TODO: Create a tuple with your favorite colors
color = ("Orange", "Yellow", "Blue")
print(color)

# TODO: Try to modify one of the colors (this should raise an error) 

# TODO: Count how many times a specific color appears in the tuple
taille = len(color)
print("taille du Tuple: ", taille)

# TODO: Find the index of a specific color
print("Index of Yellow", color.index("Yellow"))
# TODO: Create a new tuple by concatenating two existing tuples
newcolor = ("green", "black")
join = color + newcolor
print(join)

# Print the results of each operation

print("------------------------ Exercice 3 -----------------------------------")

# TODO: Create a dictionary representing a person (name, age, city)
person = {
    "name": "Ali",
    "age": 25,
    "city": "Paris"
}
print(person)

# TODO: Add a new key-value pair for the person's occupation
person["occupation"] = "Etudiant"
print("adding new occupation", person)

# TODO: Update the person's age

person["age"] = 26
print("New age update", person)


# TODO: Remove the 'city' key-value pair
person.pop("city")
print("bye bye City :(", person)


# TODO: Print all keys, then all values
x = 0
for key in person:
    x = x + 1
    print(" key ", x, key)

# TODO: Check if a specific key exists in the dictionary
print("Getting my name ", person.get("name"))
# Print the final dictionary