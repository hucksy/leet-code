import bisect

def longest_substring(s: str) -> int:
    max_string_length = 0
    cur_string = []

    for i, val in enumerate(s):
        if val not in cur_string:
            cur_string.append(val)
            if(len(cur_string) > max_string_length):
                max_string_length = len(cur_string)
        else:
            cut_index = cur_string.index(val) + 1
            cur_string = cur_string[cut_index:]
            cur_string.append(val)
    
    return max_string_length


def longest_substring_2(s: str) -> int:
    max_string_length = 0
    sub_string = []
    start_index = 0
    char_dict = {}

    for i, val in enumerate(s):
        if val in char_dict and start_index <= char_dict[val]: 
            start_index = char_dict[val] + 1
            char_dict[val] = i
        else: 
            char_dict[val] = i
            max_string_length = max(max_string_length, i-start_index + 1)

    return max_string_length


test = "abcabcbb"

print(longest_substring_2(test))



