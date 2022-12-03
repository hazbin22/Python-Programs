n=int(input("Enter the limit:"))
print("Enter the colors: ")
clr1=[]
clr2=[]
for i in range(0,n):
    x=input()
    clr1.append(x)
print("clr1= ",clr1)
n=int(input("Enter the limit:"))
print("Enter the colors: ")
for i in range(0,n):
    y=input()
    clr2.append(y)
print("clr2= ",clr2)
print("Color that are not common: ")
for color in clr1:
    if color not in clr2:
        print(color)
