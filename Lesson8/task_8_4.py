from typing import Optional, Tuple


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


text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea."""

my_email = 'scitaxapp@gmail.com'

# 1. combining text and my_email
new_text = f'{text} \n {my_email}'

# 2.-3. calculating letters and vowels in text
print(calc_letters_vowels(text))

# 4. Printing every 18-th symbol converted form uppercase to lower and opposite
count = 0
for letter in text[17::18]:
    count += 18
    print(f'{count} {letter}')
