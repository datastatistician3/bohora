import string

def is_palindrome(s, remove_punctuation=False):
    """
    This function checks if the given string is a palindrome.
    A palindrome is equal to its reverse, for example "rotor" or "racecar".
    
    :param s: s is an input string
    :param remove_punctuation: remove_punctuation is a boolean whether to remove punctuation or not
    
    :return: A boolean True if the string is palindrome
    
    Usage:
        >>> is_palindrome("Was It A   Rat    I Saw?", remove_punctuation=True)
    """
    s = s.lower().replace(" ", "")
    if remove_punctuation:
        result = ""
        for char in s:
            if char not in string.punctuation:
                result += char
    else:
        result = s

    d = result[::-1]
    return (result == d)

print(is_palindrome("Was It A   Rat    I Saw?", remove_punctuation=True))