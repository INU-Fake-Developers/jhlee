a = int(input(""))
b = 0
c = 1
for i in range(0,a+1):
    n = b+c
    b = c
    c = n

print(b)
