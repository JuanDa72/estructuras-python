from NodeSBT import NodeSBT

class SB_tree:

    def __init__(self):
        self.root=None

    def insert(self,value):
        current=self.root
        if current is None:
            current=NodeSBT(value)

        else:
            if value<current.value:
                if current.left is None:
                    current.left=NodeSBT(value)

                else:
                    


