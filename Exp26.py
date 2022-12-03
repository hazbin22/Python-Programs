N1 = int(input("Enter the first number: "))
N2 = int(input("Enter the second number: "))
a = N1
b = N2
while N2 != N2:
    if N1 > N2:
        N1 -= N2
    else:
        N2 -= N1
print("GCD of", a, "and", b, "is", N1)