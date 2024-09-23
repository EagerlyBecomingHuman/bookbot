def main():
    file_path_to_book = "books/frankenstein.txt"
    entire_book = extract_book_contents(file_path_to_book)
    total_number_of_words = count_of_total_words(entire_book)
    char_count = count_chars_in_str(entire_book)
    unsorted_list = convert_dict_to_list(char_count)
    sorted_list = sorted(unsorted_list, key=lambda x: x[1], reverse=True)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_number_of_words} words found in the document")
    print("\n")

    for each_list in sorted_list:
        print(f"The '{each_list[0]}' character was found {each_list[1]} times")
    print(f"--- End report ---")


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


def convert_dict_to_list(char_count):
    dictionary_list = []
    for key, value in char_count.items():
        if key.isalpha():
            dictionary_list.append((key, value))
    return dictionary_list


main()
