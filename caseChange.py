a=[]
b=[]
fullName=raw_input("Please enter your full name:")
for i in fullName.split(" "):
    a.append(i)

for l in a:
    new = (l.title())
    b.append(l.title())
    print(new.title())

print(b)
