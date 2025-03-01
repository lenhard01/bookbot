import sys
from stats import get_num_words, get_book_char, sort_char


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")

    num_words = get_num_words(book_contents)
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")

    book_chars = get_book_char(book_contents)
    sorted_chars = sort_char(book_chars)
    print("--------- Character Count ---------")
    for char_dict in sorted_chars:
        char = char_dict["char"]

        if char.isalpha():
            print(f"{char}: {char_dict['count']}")


if __name__ == "__main__":
    main()
