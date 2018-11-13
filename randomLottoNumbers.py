import random
x=[]
z=[]
for i in range(7):
    y=random.randint(1,59)
    x.append(y)
    if i == 6:
        print ("BONUS   : "+str(x[i]))

    else:
        print("Number "+str(i+1)+": "+str(x[i]))
f=open("dummyfile.txt","r")
print(f.read())
