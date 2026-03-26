library = []
def add_book():
book = input("Enter Book Name: ")
library.append(book)
print("Book added successfully")
def view_books():
if len(library) == 0:
print("Library is empty")
else:
print("\nAvailable Books:")
for book in library:
print(book)
def search_book():
book = input("Enter Book Name to Search: ")
if book in library:
print("Book is available in the library")
else:
print("Book not found")
def issue_book():
book = input("Enter Book Name to Issue: ")
if book in library:
library.remove(book)
print("Book issued successfully")
else:
print("Book not available")
while True:
print("\n----- Library Menu -----")
print("1. Add Book")
print("2. View Books")
print("3. Search Book")
print("4. Issue Book")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == '1':
add_book()
elif choice == '2':
view_books()
elif choice == '3':
search_book()
elif choice == '4':
issue_book()
elif choice == '5':
print("Exiting Library System")
break
else:
print("Invalid choice")
 
