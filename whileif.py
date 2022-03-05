x=int(input("Enter max number:\n"))
counter=0
for i in range(1,x):
    if x%5==0:
        counter+=1
    if i==x:
        break
print("counter is:\n", counter)
