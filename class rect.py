class rect:
    def __init__(self,breadth,length):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.breadth*self.length
    def per(self):
            return 2*(self.length+self.breadth)
a=int(input("enter the lenghth of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
obj =rect(a,b)
print("area of rectangle:",obj.area())
print("perimeter of rectangle:",obj.per())
