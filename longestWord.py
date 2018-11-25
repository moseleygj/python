print("Please end a sentence below:")
userInput=input()
i=userInput

h_num = 0

for a in i.split(" "):
    print(a)
    print(h_num)
    if len(a) >= h_num:
        h_num=len(a)
        longest_word=a


print("The longest word is: "+longest_word +"["+str(h_num)+"]")