# Import the library
from operator import itemgetter
# Define a list of books 
books = [
    {"title": "Book1", "author": "Author1", "ISBN": "111111", "genre": "Fiction"},
    {"title": "Book2", "author": "Author2", "ISBN": "222222", "genre": "Non-Fiction"},
    {"title": "Book3", "author": "Author1", "ISBN": "333333", "genre": "Fiction"},
    {"title": "Book4", "author": "Author3", "ISBN": "444444", "genre": "Non-Fiction"},
    {"title": "Book5", "author": "Author2", "ISBN": "555555", "genre": "Fiction"}
]
# Sort the books by title
print("Sorting by title:")
sorted_books = sorted(books, key=lambda x: x["title"])
for book in sorted_books:
    print(book)
    
# Sort the books by title then by author
print("\nSorting by title then by author:")
sorted_books = sorted(books, key=lambda x: (x["title"], x["author"]))
for book in sorted_books:
    print(book)

# Sort the books by genre then by author
print("\nSorting by genre then by author:")
sorted_books = sorted(books, key=lambda x: (x["genre"], x["author"]))
for book in sorted_books:
    print(book)
# Sort the books in reverse order by ISBN
print("\nSorting in reverse by ISBN:")
sorted_books = sorted(books, key=lambda x: x["ISBN"], reverse=True)
for book in sorted_books:
    print(book)
# Sort the books in place by ISBN
print("\nSorting in place by ISBN:")
books.sort(key=lambda x: x["ISBN"])
for book in books:
    print(book)
