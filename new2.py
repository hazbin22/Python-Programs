dict1={'taste':{'apple':'sweet', 'orange':'sour', 'melon':'sweet'},
       'color':{'apple':'red', 'orange':'orange', 'melon':'red'}}
count={}
for values in dict1['taste'].items():
    for values in dict1['color'].items():
        if values in count:
            count[values]+=1
        else:
            count[values]=1
print(count)
#print(dict1['taste'].get(['apple']))
