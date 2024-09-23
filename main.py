def main():
    file_path_to_book = "books/frankenstein.txt"
    entire_book = extract_book_contents(file_path_to_book)
    total_number_of_words = count_of_total_words(entire_book)
    print(total_number_of_words)


def extract_book_contents(file_path_to_book):
    with open(file_path_to_book) as f:
        return f.read()


def count_of_total_words(str_of_book_contents):
    word_count = str_of_book_contents.split()
    return len(word_count)


main()
