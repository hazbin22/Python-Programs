class moprtns:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Sum= ",self.a+self.b)
    def diff(self):
        print("Differece= ",self.a-self.b)
    def prdt(self):
        print("Product= ",self.a*self.b)
    def div(self):
        print("Quotient= ",self.a/self.b)
w=moprtns(5,6)
x=moprtns(10,5)
y=moprtns(9,5)
z=moprtns(45,5)
w.add(),x.diff(),y.prdt(),z.div()