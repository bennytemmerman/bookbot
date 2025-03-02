import sys
from stats import count_words, character_count, sorted_character_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

char_count = {}
book_path = sys.argv[1]

def get_book_text(path: str) -> str:
    """Reads and returns the content of a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")
    char_count = character_count(book_text)
    print(char_count)
    sorted_chars = sorted_character_counts(char_count)
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

main()
