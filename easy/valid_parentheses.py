def is_valid_parenthesis(s: str) -> bool:
    symbol_stack = []
    symbol_map = {"(":")", "[":"]", "{":"}"}
    for i, p in enumerate(s):
        if p in symbol_map:
            symbol_stack.append(p)
        elif p in symbol_map.values():
            if symbol_stack == [] or p != symbol_map[symbol_stack.pop()]:
                return False
    return symbol_stack == []


s = "()(())"
print(is_valid_parenthesis(s=s))