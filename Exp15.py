list1=[4,7,5,3]
list2=[7,4,9,2,5]
x=len(list1)
y=len(list2)
if x==y:
    print("Lenth of the lists are equal.")
else:
    print("Length of list are not equal.")
a=sum(list1)
b=sum(list2)
if a==b:
    print("Sum are same")
else:
    print("Sum are not same")
count=0
for x in list1:
    for y in list2:
        if(x==y):
            count=1
if(count==1):
    print("There is common element.")
else:
    print("There is no common element.")