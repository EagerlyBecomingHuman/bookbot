def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = open_file(path_to_file)
    print(file_contents)


def open_file(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
        return book_contents


main()
