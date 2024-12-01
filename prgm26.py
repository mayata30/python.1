print("rectangle")
print(".....")
l=int(input("enter a lenght of the rectangle:"))
b=int(input("enter breadth of rectangle:"))
area=lambda l,b:l*b
print("area of rectangleis",area(l,b))
per=lambda l,b:2*(l+b)
print("per of rectangle is",per(l,b))
print("square")
print(".....")
a=int(input("enter a length of one side of square:"))
area=lambda a:a*a
print("are of square is",area(a))
per=lambda a:4*a
print("per of square is",per(a))
