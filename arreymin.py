x=int(input("Enter max number\n"))
l=[]
p=0; m=0
for i in range(0,x):
    s=int(input("Enter element\n"))
    l.append(s)
    if i==x:
        break
print("added done\n")
for y in l:
    p=l[0]
    if p<y:
        p=m
        break
print("min is\n")
print(m)
        
