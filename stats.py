def get_num_words(contents: str):
    words = contents.split()
    word_count = len(words)
    return word_count


def get_num_letters(contents: str):
    num_letters = {}
    words = contents.split()
    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter in num_letters:
                num_letters[lower_letter] += 1
            else:
                num_letters[lower_letter] = 1
    return num_letters


def get_num_letters_sorted(num_letters: dict):
    num_letters_arr = []
    for letter_key in num_letters:
        num_letters_arr.append(
            {"character": letter_key, "count": num_letters[letter_key]}
        )
    num_letters_arr.sort(reverse=True, key=(lambda x: x["count"]))
    return num_letters_arr
