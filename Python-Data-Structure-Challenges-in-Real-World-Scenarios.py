# Task 1: Library System Enhancement:
def add_book(library, new_book):
    if new_book not in library:
        library.append(new_book)
        print(f'Book "{new_book[0]}" by {new_book[1]} added to the library.')
    else:
        print(f'Book "{new_book[0]}" by {new_book[1]} is already in the library.')

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding a new book
add_book(library, ("Fahrenheit 451", "Ray Bradbury"))

# Trying to add a duplicate book
add_book(library, ("1984", "George Orwell"))

print(library)