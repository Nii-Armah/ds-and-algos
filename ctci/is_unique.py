"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s: str) -> bool:
    s = s.lower()
    return len(set(s)) == len(s)


# Without Data Structure
def is_unique_alt(s: str) -> bool:
    s = sorted(s.lower())

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True
