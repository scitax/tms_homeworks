from typing import Optional, Tuple
import this


def calc_letters_vowels(string: Optional[str]) -> Tuple[int, int]:
    vowels_letters = ['a', 'A', 'e', 'E', 'y', 'Y', 'i', 'I', 'o', 'O']
    letter_count = 0
    vowels_count = 0
    for letters in string:
        if letters.isalpha():
            letter_count += 1
        if letters in vowels_letters:
            vowels_count += 1
    return letter_count, vowels_count


text = "".join([this.d.get(c, c) for c in this.s])

my_email = 'scitaxapp@gmail.com'

# 1. combining text and my_email
new_text = f'{text} \n {my_email}'

# 2.-3. calculating letters and vowels in text
print(calc_letters_vowels(text))

# 4. Printing every 18-th symbol converted form uppercase to lower and opposite
count = 0
for letter in text[17::18]:
    count += 18
    print(f'{count} {letter.swapcase()}')
