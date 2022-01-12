test1=[]
test2=[]
init=0
a=int(input("Enter a number here")) # this is given integer N 
for x in range(a):
    temp=""
    for y in range(a):
        init+=1
        if y==a-1:
            temp+=(str(init))
        else:
            temp+=(str(init)+"*")
    if x%2==0:
        test1.append(temp)
    else:
        test2.insert(0,temp)
test=test1+test2
for x in test:
    print(x)