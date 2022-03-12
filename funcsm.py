def sm(x,y):
    for i in x:
        y=y+i
        if i==x:
            break
    return y
x=int(input("Enter x:\n"))
y=0
print(sm(x,y))
