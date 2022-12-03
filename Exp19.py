n=int(input("Enter the size: "))
print("Enter the elements: ")
l1=[]
l2=[]
for i in range(0,n):
    ele=int(input())
    l1.append(ele)
    if ele%2!=0:
       l2.append(ele)
print(l1)
print(l2)