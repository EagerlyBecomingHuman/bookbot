def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = open_file(path_to_file)
    word_count_in_file = count_words(file_contents)
    character_count_in_file = count_characters(file_contents)

    print(f"There are {word_count_in_file:,} words in this book. \n")
    print(character_count_in_file)


def open_file(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
        return book_contents


def count_words(file_contents):
    book_of_words = file_contents.split()
    return len(book_of_words)


def count_characters(file_contents):
    character_dictionary = {}
    for each_character in file_contents:
        lowercase_characters = each_character.lower()
        if lowercase_characters in character_dictionary:
            character_dictionary[lowercase_characters] += 1
        else:
            character_dictionary[lowercase_characters] = 1
    return character_dictionary


main()
