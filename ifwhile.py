x=int(input("Enter max number :\n"))
while x<=100:
    if x<30:
        print("fizz:\n")
        break
    elif x<70:
        print("buzz\n")
        break
    else:
        print("fizz-buzz\n")
        break
    if x==100:
        break
