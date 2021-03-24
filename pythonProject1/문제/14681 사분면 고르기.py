a=int(input("x값은?"))
b=int(input("y값은?"))
if a>0 and b>0:
    print("1")
elif a>0 and b<0:
    print("4")
elif a<0 and b>0:
    print("2")
elif a<0 and b<0:
    print("3")