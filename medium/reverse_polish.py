from collections import deque
from typing import List


def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def multiply(a: int, b: int):
    return a * b 

def divide(a: int, b: int):
    return a // b

def eval_RPN(tokens: List[str]) -> int:
    stack = deque()
    for token in tokens:
        breakpoint()
        if token.lstrip("-").isnumeric():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(add(operand1, operand2))
            elif token == "-":
                stack.append(subtract(operand1, operand2))
            elif token == "*":
                stack.append(multiply(operand1, operand2))
            elif token == "/":
                stack.append(divide(operand1, operand2))
    return stack[0]


test = ["2","1","+","3","*"]
test2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
test3 = ["4","13","5","/","+"]
print(eval_RPN(test2))


"""
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
