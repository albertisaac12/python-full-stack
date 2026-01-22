class Calc:
    def _init__(self):
        print("This is a calcualtor")
    def add(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def mod(self,x,y):
        return x//y
    def sub(self,x,y):
        return x-y

a = int(input("App kon: "))
b = int(input("mei inssan: "))

c = Calc()
print(c.add(a,b))