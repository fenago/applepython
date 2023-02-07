import csv

# sample data
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'ISBN': '9780743273565', 'genre': 'Novel'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'ISBN': '9780446310789', 'genre': 'Novel'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'ISBN': '9780140390725', 'genre': 'Novel'},
    {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'ISBN': '9780679728776', 'genre': 'Autobiography'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'ISBN': '9780316769488', 'genre': 'Novel'}
]

# write the data to a csv file
with open('book.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'author', 'ISBN', 'genre'])
    writer.writeheader()
    for book in books:
        writer.writerow(book)
