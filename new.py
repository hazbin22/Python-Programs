dict1={"vegetable":5, "fruits":5, "cars":6}
count={}
for values in dict1.values():
    if values in count:
        count[values]+=1
    else:
        count[values]=1
print(count)