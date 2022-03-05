x=int(input("Enter max number:\n"))
sm=0 
for i in range(0,x):
    sm=sm+i
    if i==x:
        break
print("sum is\n", sm)
