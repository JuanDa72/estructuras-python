from node import node

class linkedList:

  def __init__(self):
    self.head=None
    self.size=0


  def append(self,value):
    myNode=node(value)

    if self.size==0:
      self.head=myNode

    else:
      current=self.head
      while current.next!=None:
        current=current.next

      current.next=myNode
      current=current.next
      current.next=None


    self.size+=1


  def remove(self,value):
    current=self.head
    if self.size==0:
      return False

    elif current.value==value:
      self.head=current.next

    else:
      current=self.head
      try:
        while current.next.value!=value:
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
    while current!=None:
      string_one+=str(current)
      if current.next!=None:
        string_one+=str(", ")
      current=current.next


    string_one+="|"
    return string_one



  def rating(self,value):
    counter=1
    list=[]
    current=self.head
    while current!=None:
      if current.value==value:
         list.append(counter)

      current=current.next
      counter+=1

    if len(list)==0:
      return False

    else:
      return list


  def __iter__(self):
    current=self.head
    while current!=None:
      yield current
      current=current.next






'''
myList=linkedList()

myList.append(5)
myList.append("oh")
myList.append("flow")
myList.append(1)
myList.append(8)
myList.remove("flow")
myList.append(5)
print(myList)
print(len(myList))
print(myList.rating(5))
for i in myList:
  print(i)

'''

lista=linkedList()
for i in lista:
  print("hola")




