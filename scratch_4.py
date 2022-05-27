class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, o):
        print("First input complex number:",o.a)
        print("Second input complex number:",o.b)
        print(self.a + o.a,"+",self.b+ o.b,"j")


c1 = ComplexNum(1,2)
c2 = ComplexNum(3,4)

c1+c2
