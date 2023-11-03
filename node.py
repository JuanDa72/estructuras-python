class node:

    def __init__(self,value):
        self.value=value
        self.next=None


    def __str__(self):
        return str(self.value)


#Cada elemento en una lista enlazada puede considerarse como un nodo, este tiene un valor y una conexión
    #con el siguiente elemento, inicialmente es none


#nodo=node("gla")
#print(nodo)