class NodeHT:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

    def __str__(self):
        return str(str(self.key)+":"+str(self.value))
