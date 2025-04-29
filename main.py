from stats import get_number_of_words, get_each_character_count, get_sorted_dicts
import sys

def get_book_text(book_path: str) -> str:
    with open(book_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def print_report(word_count: int, sorted_dicts: list, book_path: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dicts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_number_of_words(book_text)
    character_count = get_each_character_count(book_text)
    list_of_dicts = get_sorted_dicts(character_count)
    print_report(word_count, list_of_dicts, book_path)

if __name__ == "__main__":
    main()
