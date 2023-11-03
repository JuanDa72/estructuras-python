from LinkedList import linkedList

class cola:

    def __init__(self):
        self.cola=linkedList()


    def isEmpty(self):
        if self.cola.size==0:
            return True

        else:
            return False


    def enqueue(self,value):
        self.cola.append(value)


    def front(self):
        return self.cola.head


    def rear(self):
        current = self.cola.head

        if current is None:
            return False

        else:
            while current.next != None:
                current = current.next

            return current


    def dequeue(self):
        current=self.cola.head
        if current is None:
            return False

        else:
            self.cola.head=current.next
            self.cola.size-=1


    def __str__(self):
        return self.cola.__str__()


    def __iter__(self):
        current=self.cola.head
        while current is not None:
            yield current.value
            current=current.next


    def __len__(self):
        return len(self.cola)


    def rating(self,value):
        return self.cola.rating(value)






cc=cola()
cc.enqueue(2)
cc.enqueue(1)
cc.enqueue(10)
cc.enqueue(5)
cc.enqueue(20)
print(cc)
print(len(cc))
#Hasta este momento todo funciona acordemente, incluyendo el metodo que imprime

#Intento de eliminar un elemento
print()
cc.dequeue()
print(cc)
print(len(cc))
cc.enqueue(1)
print(cc.rating(1))
print()
for i in cc:
    print("xd")
#Parece que si funciona xd
#Luego de unas pruebas no muy intensivas, parece que todo funciona