
print("------------------------ Exercice 1 ----------------------------------- \n")
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
print("\n")

print("------------------------ Exercice 2 ----------------------------------- \n")
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

print("\n")

print("------------------------ Exercice 3 ----------------------------------- \n")

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
print("\n")

print("------------------------ Exercice 4 ----------------------------------- \n")

# TODO: Create two sets of numbers
set1 = {1, 2, 3}
set2 = {2, 3, 4, 5}


print("my Sets :\n", set1)
print("", set2)
# TODO: Find the union of the two sets
print("union of my sets: \n", set1.union(set2))

# TODO: Find the intersection of the two sets

print("intersection of my sets: \n", set1.intersection(set2))
# TODO: Find the difference between the first and second set
print("difference between my sets: \n ", set1.difference(set2))

# TODO: Add a new element to one of the sets
print("Adding a new element to set1\n ", set1.add(6), set1)

# TODO: Remove an element from one of the sets
print("Removing an element from set2\n", set2.remove(4), set2)
print("\n")

# Print the results of each operation
print("------------------------ Exercice 5 ----------------------------------- \n")

# TODO: Create a list of dictionaries representing books (title, author, year)
books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"title": "1984", "author": "George Orwell", "year": 1949}
]
print("\nMy list of books :\n", books)

print("\n--- un peu mieux a voire non ! :) --- \n")
for book in books:
    print(f"{book['title']} by {book['author']} ({book['year']})")

# TODO: Add a new book to the list

books.append({"title": "Le Prince", "author": "Machiavelli", "year": 1997})
print("\nnew liste of books", books)

# TODO: Sort the list of books by year
books.sort(key=lambda book: book["year"])

for book in books:
    print(f"{book['title']} by {book['author']} ({book['year']})")


bibliotheque = {
    "Robert Greene": ["48 Laws of Power", "The 50th Law", "The Art of Seduction"],
    "Machiavelli": ["Le Prince", "Art of War"]
}
author = "Robert Greene"
# Print all books by this author
if author in bibliotheque:
    print(f"Books by {author}:")
    for book in bibliotheque[author]:
        print("-", book)
else:
    print(f"{author} not found in the library.")
# Print the final nested data structure