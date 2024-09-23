def main():
    file_path_to_book = "books/frankenstein.txt"
    entire_book = extract_book_contents(file_path_to_book)
    total_number_of_words = count_of_total_words(entire_book)
    char_count = count_chars_in_str(entire_book)
    print(char_count)


def extract_book_contents(file_path_to_book):
    with open(file_path_to_book) as f:
        return f.read()


def count_of_total_words(str_of_book_contents):
    word_count = str_of_book_contents.split()
    return len(word_count)


def count_chars_in_str(str_of_book_contents):
    char_dict = {}
    for each_char in str_of_book_contents:
        lower_case = each_char.lower()
        if lower_case in char_dict:
            char_dict[lower_case] += 1
        else:
            char_dict[lower_case] = 1
    return char_dict


main()
