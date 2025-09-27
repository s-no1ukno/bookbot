import sys
from stats import get_character_count, get_word_count, sort_character_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    # exit gracefully if args not provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    word_count = get_word_count(get_book_text(path))

    char_count = get_character_count(get_book_text(path))
    sorted = sort_character_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted:
        print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")


main()
