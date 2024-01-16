class NodeSBT():

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.value)

    def check_space(self, node):
        if node.left is None or node.right is None:
            return True

        else:
            return False
