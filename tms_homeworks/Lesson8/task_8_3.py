from typing import Optional


def palindrome(*args: Optional[str]) -> Optional[list]:
    """
    defines palindrome words (words that are written the same for both directions)
    :param args: str
    :return: list of palindrome words
    """
    palindrome_list = []
    for word in args:
        if not isinstance(word, str):
            pass
        elif word == word[::-1]:
            palindrome_list.append(word)
    return palindrome_list
