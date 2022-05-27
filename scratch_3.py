class a:
    def __init__(self):
        self.n = int(input("Enter Number of elements:"))
        self.l = []
        print("---Enter the list elements---")
        for i in range(self.n):
            self.p = int(input("Enter the list element:"))
            self.l.append(self.p)
        print("The list is as follows:",self.l)
class b(a):
    def Largest(self):
        l= self.l
        maxi = max(l)
        print("Largest element is:",maxi)
class c(a):
    def Smallest(self):
        mini = min(self.l)
        print("Smallest element is:",mini)
obj1 = a()
obj2 = b()
obj1.Largest()
