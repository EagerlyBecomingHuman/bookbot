def main():
    file_path_to_book = "books/frankenstein.txt"
    entire_book = extract_book_contents(file_path_to_book)
    print(entire_book)


def extract_book_contents(file_path_to_book):
    with open(file_path_to_book) as f:
        return f.read()


main()
