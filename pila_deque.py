import collections

class pila_deque:

    def __init__(self):
        self.stack=collections.deque()


    def isEmpty(self):
        if len(self.stack)==0:
            return True

        else:
            return False


    def push(self,value):
        self.stack.append(value)


    def peek(self):
        if len(self.stack)==0:
            return False

        else:
            a = self.stack[-1]
            return a


    def pop(self):
        self.stack.pop()

    def __str__(self):
        lista=list(self.stack)
        return str(lista)


    def __len__(self):
        return len(self.stack)


    def toCopy(self):
        return collections.deque(self.stack)


    def rating(self,value):
        return self.stack.index(value)+1


    def __iter__(self):
        for i in self.stack:
            yield i



pila=pila_deque()
print(pila.peek())