from typing import List

def generateParenthesis(self, n: int) -> List[str]:

    paren_list = []

    def gen_paren(cur_string, n, paren, stack):
        if n == 0 and not stack:
            return cur_string

        if n > 0:
            cur_string += "("
            stack.append(")")
            paren_list.append(gen_paren(cur_string, n-1, stack))
        if stack:
            cur_string += stack.pop()
            paren_list.append(gen_paren(cur_string, n, stack)

    paren_list = gen_paren("(", n-1, ")") == "()()"
