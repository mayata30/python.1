n=int(input("enter the number:"))
count=0
num=2
while count<n:
    is_prime=True
    for i in range(2,num-1):
        if(num%i==0):
             is_prime=False
             break
    if is_prime:
                print(num)
                count=count+1
    num=num+1
                
