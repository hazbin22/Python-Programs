string1 = input("Enter the string: ")
if (string1[-3:]=='ing'):
  string1+='ly'
else:
  string1 += 'ing'
print(string1)
string2 = input("Enter the string: ")
if (string2[-3:]=='ing'):
  string2+='ly'
else:
  string2+='ing'
print(string2)