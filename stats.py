def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_dict: dict[str, int]) -> list[dict[str, int]]:
    char_list = [{"char": char, "num": count} for char, count in char_dict.items() if char.isalpha()]
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
