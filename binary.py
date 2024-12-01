binary=input("enter a bimary no:")
decimal=0
for digit in binary:
    decimal=decimal*2+int(digit)
print("the decimal equivalent of",binary,"is",decimal)
