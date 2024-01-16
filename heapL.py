class heapL:

    def __init__(self):
        self.list=[]
        self.size = len(self.list)
        self.root=None


    def peek_min(self):
        return self.root


    def insert(self,value):
        if len(self.list)==0:
            self.list.append(value)
            self.root=self.list[0]

        else:
            self.list.append(value)
            counter=len(self.list)-1
            while counter>0:
                n_son=self.list[counter]
                n_father=(counter-1)//2
                if self.list[n_father]<=n_son:
                    counter-=1

                else:
                    self.list[counter]=self.list[n_father]
                    self.list[n_father]=n_son
                    counter-=1
                    
        self.root=self.list[0]


    def extract_min(self):
        self.list.pop(0)
        counter = len(self.list) - 1
        while counter > 0:
            n_son = self.list[counter]
            n_father = (counter - 1) // 2
            if self.list[n_father] <= n_son:
                counter -= 1

            else:
                self.list[counter] = self.list[n_father]
                self.list[n_father] = n_son
                counter -= 1

        self.root = self.list[0]


    def __len__(self):
        return len(self.list)


    def is_empty(self):
        return True if len(self.list)==0 else False


    def __iter__(self):
        for i in self.list:
            yield(i)


    def build_heap(self,list:list):
        self.list=list
        counter = len(self.list) - 1
        max=(counter-1)//2
        for i in range(0,max+1):
            son_left=2*i+1
            son_right=2*i+2
            father=self.list[i]
            if father<=self.list[son_left] and father<=self.list[son_right]:
                continue

            elif father>=self.list[son_left] and father<=self.list[son_right]:
                self.list[i]=self.list[son_left]
                self.list[son_left]=father

            elif father <= self.list[son_left] and father >= self.list[son_right]:
                self.list[i]=self.list[son_right]
                self.list[son_right]=father

            elif father >= self.list[son_left] and father >= self.list[son_right]:
                if self.list[son_left]==self.list[son_right]:
                    self.list[i]=self.list[son_left]
                    self.list[son_left]=father

                else:
                    check=[self.list[son_left],self.list[son_right]]
                    m=min(check)
                    change=son_left if self.list[son_left]==m else son_right
                    self.list[i]=self.list[change]
                    self.list[change]=father


            counter = len(self.list) - 1
            while counter > 0:
                n_son = self.list[counter]
                n_father = (counter - 1) // 2
                if self.list[n_father] <= n_son:
                    counter -= 1

                else:
                    self.list[counter] = self.list[n_father]
                    self.list[n_father] = n_son
                    counter -= 1

            self.root = self.list[0]



    def __str__(self):
        return str(self.list)









prueba1=heapL()
prueba1.build_heap([7, 2, 9, 1, 5, 3, 6, 4, 8])
print(prueba1)