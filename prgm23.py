name=[]
n=int(input("enter the number of student:"))
for i in range(1,n+1):
	print("enter name:",i)
	item=str(input())
	name.append(item)
print(name)
name.sort()
print("alphabetical order:",name)
