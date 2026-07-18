import sys
from pathlib import Path

from stats import chars_dict_to_sorted_list, count_characters, get_num_words


def get_book_text(filepath: str) -> str:
    with Path(filepath).open("r", encoding="utf-8") as file:
        return file.read()


def print_report(book_path: str, num_words: int, sorted_chars: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text.lower())
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print_report(book_path, num_words, sorted_chars)


if __name__ == "__main__":
    main()
