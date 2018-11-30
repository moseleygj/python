def getUserAnswer(prompt):
    while a=0:
        answer=input("Please enter yes or no:").lower().strip()
        if answer in ("yes","no"):
         return "Your answer was valid"
         a=1
         break
    
print(getUserAnswer("Yes or No"))