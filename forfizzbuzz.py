x=int(input("Enter max number:\n"))
for i in range(0,x):
    if i%2==0:
        print("fizz\n")
    elif i%5==0:
        print("buzz\n")
    else:
        print("fizz-buzz\n")
    if i==x:
        break
