from LinkedList import linkedList

class stack:

    def __init__(self):
        self.stack=linkedList()


    def isEmpty(self):
        if len(self.stack)==0:
            return True

        else:
            return False


    def push(self,value):
        self.stack.append(value)


    def peek(self):
        current = self.stack.head

        if current is None:
            return False

        else:
            while current.next != None:
                current = current.next

            return current


    def pop(self):
        acc=self.stack.head

        if acc is None:
            return False

        else:
            while acc.next is not None:
                acc = acc.next

        self.stack.remove(acc.value)


    def __str__(self):
        return self.stack.__str__()



    def __len__(self):
        return self.stack.__len__()


    def rating(self,value):
        return self.stack.rating(value)


    def __iter__(self):
        return self.stack.__iter__()



pila=stack()
pila.push(2)
pila.push(3)
pila.push(4)
pila.pop()
pila.push(10)
pila.push(11)
print(pila.peek())
print(pila)