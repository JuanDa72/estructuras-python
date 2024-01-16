import LinkedListHT
from LinkedListHT import LinkedListHT
class hashTable:

    def __init__(self,capacity):
        self.capacity=capacity
        self.list=[None]*capacity

    def hash_function(self,key):
        if type(key)==str:
            sum=0
            for i in key:
                sum+=ord(i)

            return sum%self.capacity

        elif type(key)==int:
            return key%self.capacity

        elif type(key)==float:
            return int(key)%self.capacity

        elif type(key)==bool:
            string=str(key)
            sum=0
            for i in string:
                sum+=ord(i)

            return sum%self.capacity


    def insertion(self,key,value):
        index=self.hash_function(key)
        if self.list[index] is None:
            myLinked=LinkedListHT()
            myLinked.append(key,value)
            self.list[index]=myLinked

        elif isinstance(self.list[index],LinkedListHT):
            self.list[index].append(key,value)



    def __len__(self):
        return len(self.list)

    def get(self,key):
        index = self.hash_function(key)
        myLinked=self.list[index]
        if self.list[index] is None:
            return False

        elif len(myLinked)==1 and key==myLinked.head.key:
            return myLinked.head.value

        elif len(myLinked)==1 and key!=myLinked.head.key:
            return False

        else:
            current=myLinked.head
            try:
                while current.key!=key:
                    current = current.next

                return current.value

            except AttributeError:
                return False

    def contain(self,key):
        index = self.hash_function(key)
        myLinked = self.list[index]
        if self.list[index] is None:
            return False

        elif len(myLinked) == 1 and key == myLinked.head.key:
            return True

        elif len(myLinked) == 1 and key != myLinked.head.key:
            return False

        else:
            current = myLinked.head
            try:
                while current.key != key:
                    current = current.next

                return True

            except AttributeError:
                return False


    def remove(self,key):
        index=self.hash_function(key)
        myLinked=self.list[index]
        red=False

        if self.list[index] is None:
            return False

        elif len(myLinked)==1 and myLinked.head.key==key:
            myLinked.remove(key)
            return True

        else:
            for i in myLinked:
                if i==key:
                    myLinked.remove(key)
                    red=True

            return True if red else False





has=hashTable(5)
print("yogurt"+ " "+ str(has.hash_function("yogurt")))
has.insertion("yogurt",3000)
print(has.hash_function("agua"))
has.insertion("agua",1)
print(has.hash_function("miel"))
has.insertion("miel",8000)
print(has.hash_function("sal"))
has.insertion("sal",4000)
print(has.hash_function("jalea"))
has.insertion("jalea",50000)
print(has.list)
print(has.remove("jalea"))
print(len(has.list[4]))
#print(has.contain("yogurt"))
