from stats import get_book_word_count, get_character_count, get_sorted_character_dicts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # file_path = 'books/frankenstein.txt'
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_book_word_count(book_text)
    character_count = get_character_count(book_text)
    character_dicts = get_sorted_character_dicts(character_count)
    print_report(character_dicts, word_count, file_path)

def print_report(character_dicts, word_count, file_path):
    alpha_dicts = [i for i in character_dicts if i["char"].isalpha() == True]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in alpha_dicts:
        print(f"{i['char']}: {i['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()