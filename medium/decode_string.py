
def decode_string(s: str) -> str:
    """
    Input: "3[a2[c]]e"
    Output: "accaccacce"
    
    if letter != ]:
        push to stack
    if letter == ]:
        cur_l = stack.pop
        cur_s += cur_l
        while cur_l != [:
            cur_s += stack.pop
            cur_l = stack.pop
        repeat = stack.pop
        cur_s = repeat * stack.pop
        for l in cur_s
            stack.push(s)
    while 
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