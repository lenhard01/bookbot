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


def sort_on(char_count_tuple: tuple[str, int]) -> int:
    return char_count_tuple[1]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list: list[tuple[str, int]] = []
    for char in num_chars_dict:
        count = num_chars_dict[char]
        chars_list.append((char, count))
    return sorted(chars_list, reverse=True, key=sort_on)
