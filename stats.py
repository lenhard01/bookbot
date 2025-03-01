def get_num_words(text):
    return len(text.split())


def get_book_char(text):
    char_counts = {}

    for char in text:
        char = char.lower()

        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


def sort_char(char_counts):
    # Convert a dictionary to a list of dictionaries
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})

    # Define a function to tell sort() which value to sort by
    def sort_on(dict_item):
        return dict_item["count"]

    # Sort the list from highest count to lowest count
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
