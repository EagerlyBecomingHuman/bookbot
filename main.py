def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = open_file(path_to_file)
    word_count_in_file = count_words(file_contents)

    # print(file_contents)
    print(f"There are {word_count_in_file:,} words in this book.")


def open_file(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
        return book_contents


def count_words(file_contents):
    book_of_words = file_contents.split()
    return len(book_of_words)


main()
