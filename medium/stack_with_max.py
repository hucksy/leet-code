from collections import deque

class MaxStack:

    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if self.max_stack:
            if val >= self.max_stack[0]:
                self.max_stack.appendleft(val)
            else:
                self.max_stack.appendleft(self.max_stack[0])
        else:
            self.max_stack.appendleft(val)

    def pop(self) -> int | None:
        if self.stack:
            self.max_stack.pop()
            return self.stack.pop()
        else:
            return None
    
    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack)-1]
        else:
            return 0

    def get_max(self) -> int:
        if self.stack:
            return self.max_stack[0]
        else:
            return 0


ms = MaxStack()
ms.push(2)
ms.push(5)
print(ms)
print(f"max = {ms.get_max()}")
ms.push(99)
print(f"max = {ms.get_max()}")
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.pop())
