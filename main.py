import sys
from stats import get_num_words, get_num_letters, get_num_letters_sorted


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    contents = get_book_text(file_path)
    num_words = get_num_words(contents)
    num_letters = get_num_letters(contents)
    sorted_num_letters = get_num_letters_sorted(num_letters)

    print(f"{' BOOKBOT ':=^33}")
    print(f"Analyzing book found at {file_path}...")
    print(f"{' Word Count ':-^33}")
    print(f"Found {num_words} total words")
    print(f"{' Character Count ':-^33}")
    for character_dict in sorted_num_letters:

        character = character_dict["character"]
        count = character_dict["count"]

        if character.isalpha():
            print(f"{character}: {count}")

    print(f"{' END ':=^33}")


if __name__ == "__main__":
    main()
