
def decode_string(s: str) -> str:
    """
    Input: s = 3[a2[c]]e -> 3[acc]e ->  accaccacc
    Output: "accaccacce"

    decode(cur_string):
        if len(cur_string) == 1:
            return cur_string
        if number:
            repeat = number
            move past [
            move and add letters until "]" to build phrase
            cur_s += (repeat * decode(phrase) + decode(remaining)
        if letter:
            return letter + decode(remaining)
    """
    breakpoint()
    if len(s) == 1:
        return s
    if s[0].isalpha():
        return s[0] + decode_string(s[1:len(s)])
    if s[0].isnumeric():
        repeat = int(s[0])
        sub_phrase = ""
        i = 2 # start after the "[""
        while s != "]" and s[i].isalpha():
            sub_phrase += s[i]
            i += 1
        new_s = sub_phrase * repeat
        return decode_string(new_s + s[i-1:])


s = "3[a2[c]]e"

print(decode_string(s))