student={}
i=[]
n=int(input("enter the number of sudent:"))
for i in range (0,n):
	name=input("Enter the name:")
	age=input("enter the age:")
	grade=input("enter the grade:")
	student[name]=age,grade
print(student)
