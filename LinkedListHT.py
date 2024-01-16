from NodeHT import NodeHT

class LinkedListHT:

    def __init__(self):
        self.head=None
        self.size=0

    def append(self,key,value):
        myNode=NodeHT(key,value)

        if self.size==0:
            self.head=myNode

        else:
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=myNode
            current=current.next
            current.next=None

        self.size+=1


    def remove(self,key):
        current=self.head

        if self.size==0:
            return False

        elif current.key==key:
            #print("elif")
            self.head=current.next

        else:
            try:
                while current.next.key!=key:
                    #print("jfjjfjfjf")
                    current=current.next

                deletedNode=current.next
                current.next=deletedNode.next

            except AttributeError:
                return False

        self.size-=1

    def __len__(self):
        return self.size


    def __str__(self):
        string_one="|"
        current=self.head
        while current is not None:
            string_one+=str(current)
            if current.next is not None:
                string_one+=", "

            current=current.next

        string_one+="|"
        return string_one


    def __iter__(self,selection=1):
        if selection==1:
            current=self.head
            while current is not None:
                yield current.key
                current=current.next

        elif selection==2:
            current=self.head
            while current is not None:
                yield current.value
                current=current.next




new=LinkedListHT()
new.append("tren",5)
new.append("Julian",0)
new.append("city",2)
#print(new)




