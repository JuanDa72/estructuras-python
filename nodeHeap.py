class nodeHeap():

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.number=0

    def __str__(self):
        return str(self.value)