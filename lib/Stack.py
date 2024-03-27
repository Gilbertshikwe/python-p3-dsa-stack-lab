class Stack:

    def __init__(self, items=[], limit=100):
        self.limit = limit
        self.items = items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit == len(self.items)

    def search(self, target):
        if self.isEmpty():
            return -1
        else:
            for i, item in enumerate(self.items[::-1]):
                if item == target:
                    return i
            return -1
stack = Stack()
print(stack.isEmpty()) 
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  
print(stack.size())  
print(stack.full())  
print(stack.search(2))  







