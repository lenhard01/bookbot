import sys
from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath: str) -> str:
    with open(filepath, 'r', encoding = 'utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text.lower())
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
if __name__ == "__main__":
    main()
