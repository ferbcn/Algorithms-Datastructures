# queue.py
# first In - first Out

class EmptyQueueError(Exception):
    pass

class MyQueue:
    class Node:
        def __init__(self, element, _next):
            self.element = element;
            self._next = _next;

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new = self.Node(element, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail._next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty!')
        res = self.head.element
        self.head = self.head._next
        self.size -=1
        if self.is_empty():
            self.tail = None
        return res

    def top(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty!')
        return self.head.element
