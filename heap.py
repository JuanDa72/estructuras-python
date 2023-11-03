import nodeHeap

class heap():

    def __init__(self):
        self.root=None
        self.size=0

    def insert(self,value):
        myNode=nodeHeap(value)