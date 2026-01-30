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
    def kmtom(self,x): 
        return float(x*1000)
    def ctof(self,c):
        return c*(9/5) + 32
    def gbtokb(x):
        return x * 1024 * 1024
    def areasquaer(self,x):
        return x * x
    def areagola(self,x):
        return 2*3.14*x * x
a = int(input("App kon: "))
b = int(input("mei inssan: "))

c = Calc()
print(c.add(a,b))

print(c.kmtom(100))
print(c.ctof(100))

print(Calc.gbtokb(1))