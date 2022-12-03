a=int(input("Enter the limit: "))
t1=0
t2=1
print("Fibonacci Series: ")
i=3
while(i<=a):
    next=t1+t2
    print(next)
    t1=t2
    t2=next
    i+=1