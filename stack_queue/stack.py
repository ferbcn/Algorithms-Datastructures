# stack.py
# last In - first Out

class eEmptyStackError(Exception):
    pass

class MyStack:
    class Node:
        def __init__(self, element, _next):
            self.element = element;
            self._next = _next;

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty!')
        res = self.head.element
        self.head = self.head._next
        self.size -=1
        return res

    def top(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty!')
        return self.head.element
