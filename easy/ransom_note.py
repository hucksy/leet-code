def is_ransom_note(ransom_note: str, magazine: str):
    magazine_list = list(magazine)
    for i, l in enumerate(ransom_note):
        if l in magazine_list:
            magazine_list.remove(l)
        else:
            return False
    return True

rn = 'aa'
m = 'bacba'

print(is_ransom_note(rn, m))
