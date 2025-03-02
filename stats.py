def count_words(text: str) -> int:
    """Counts the number of words in a given text string using split method."""
    return len(text.split())

def character_count(text):
    char_counts = {}
    text = text.lower()  # Convert to lowercase to avoid duplicates

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sorted_character_counts(char_counts):
    char_list = [{"character": char, "count": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list
