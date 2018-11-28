n = 2
x = 15/3

Head = 1 + x + (x**2)/2 + (x**3)/6 + (x**4)/24

Tail = 0

a = 0
while a < n:
    a += 1
    Tail += (x**4)/24*(x/4)**a

result = 1/(Head+Tail)
print("p0: ", result)
print("p1: ", result*x)
print("p2: ", result*x**2/2)
print("p3: ", result*x**3/6)
print("p4: ", result*x**4/24)
print("p5: ", result*x**5/96)
temp = n+4
temp1 = x**temp*result
temp2 = 4**n*24
print("p{}: ".format(n+4), temp1/temp2)