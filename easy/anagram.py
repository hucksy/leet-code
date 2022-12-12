def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(is_anagram('frogman', 'manfrog'))
print(is_anagram('frogmam', 'manfrog'))
