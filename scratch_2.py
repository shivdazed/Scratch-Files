class family():
    def FamName(self):
        self.famname= input("Enter your Family name:")
        return
class dad:
    def FName(self):
        self.fname = input("Enter your fathers name:")
        return
class mom:
    def MName(self):
        self.mname = input("Enter your mothers name")
class son(dad,mom,family):
    def SName(self):
        self.gsname = input("Enter Your Given Name::")
        print("Your full name is: ",self.gsname,self.fname,self.famname,self.mname)
class daughter(dad,mom,family):
    def DName(self):
        self.gdname = input("Enter Your Given Name::")
        print("Your full name is: ",self.gdname,self.fname,self.famname,self.mname)



l = True
while l:
    g = input("Enter your gender:(M),(F):")
    while (g == "M" or g == "F"):
        if g == 'M':
            s = son()
            s.FamName()
            s.FName()
            s.MName()
            s.SName()
            l = False
        elif g == "F":
            d = daughter()
            d.FamName()
            d.FName()
            d.MName()
            d.DName()
            l = False
    if (g != "M" or g !="F"):
        print("invalid INput")
        l = True



