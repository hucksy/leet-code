from collections import deque

class MyQueue:

    def __init__(self):
        self.true_stack = deque()
        self.work_stack = deque()        

    def push(self, x: int) -> None:
        self.true_stack.append(x)
        self.work_stack.append(x)

    def pop(self) -> int:
        self.work_stack = deque()

        def append_recursively(popped_item):
            if len(self.true_stack) > 1:
                self.work_stack.append(append_recursively(self.true_stack.pop()))
            else:
                return self.true_stack.pop()

        if self.true_stack:
            append_recursively(self.true_stack.pop())

    def peek(self) -> int:
        while len(self.dumb_deque > 1):
            pop_item = self.dumb_deque.pop()
        self.dumb_deque = self.real_deque
        return pop_item

    def empty(self) -> bool:
        pass


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.true_stack)
print(obj.work_stack)
param_2 = obj.pop()
print(obj.true_stack)
print(obj.work_stack)
# param_3 = obj.peek()
# param_4 = obj.empty()
