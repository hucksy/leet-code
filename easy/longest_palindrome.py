
def longest_palindrome(s: str) -> int:
    singles = []
    pairs = []

    for i, l in enumerate(s):
        pass
        if l in singles:
            singles.remove(l)
            pairs.append(l)
        else:
            singles.append(l)

    single_length = 0
    if singles:
        single_length = 1
    return single_length + len(pairs) * 2


print(longest_palindrome("abaccd"))