print("Please end a sentence below:")
userInput=input()
i=userInput

h_num=0
for a in i.split(" "):
    ##print(a + " - " + str(len(a)))
    if len(a) > h_num:
        h_num=len(a)


print("The highest number is: "+str(len(a)))
