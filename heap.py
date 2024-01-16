from NodeSBT import nodeHeap

class heap():

    def __init__(self):
        self.root=None
        self.size=0


    def insert(self,value):

        while True:
            myNode = nodeHeap(value)
            if self.root is None:
                self.root = myNode
                break

            else:
                current = self.root
                if current.check_space():
                    if current.left is not None:
                        current.left = myNode
                        break

                    else:
                        current.right = myNode
                        break

                elif current.left.check_space:
                    current = current.left
                    if current.left==None:
                        current.left=myNode
                        break

                    else:
                        current.right=myNode
                        break

                elif current.right.check_space:
                    current=current.right
                    if current.left is None:
                        current.left=myNode
                        break

                    else:
                        current.right=myNode
                        break








    def __str__(self):
        #Solo una prueba, no es así el codigo final
        return str(self.root)


heap1=heap()
heap1.insert(4)
print(heap1)


