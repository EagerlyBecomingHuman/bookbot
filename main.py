def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = open_file(path_to_file)
    word_count_in_file = count_words(file_contents)
    sorted_alphabet_count = count_and_sort_alphabet_characters(file_contents)

    print(f"\n--- Report begins for {path_to_file} --- \n")
    print(f"There are {word_count_in_file:,} words in this book. \n")
    for each_finding in sorted_alphabet_count:
        print(f"The '{each_finding[0]}' character was found {each_finding[1]:,} times")
    print(f"\n--- Report ends ---\n")


def open_file(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
        return book_contents


def count_words(file_contents):
    book_of_words = file_contents.split()
    return len(book_of_words)


def count_and_sort_alphabet_characters(file_contents):
    character_dictionary = {}
    for each_character in file_contents:
        lowercase_character = each_character.lower()
        if lowercase_character.isalpha():
            if lowercase_character in character_dictionary:
                character_dictionary[lowercase_character] += 1
            else:
                character_dictionary[lowercase_character] = 1
    return sorted(
        character_dictionary.items(),
        key=lambda character_dictionary: character_dictionary[-1],
        reverse=True,
    )


main()
