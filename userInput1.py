def userInputFunc():
    while True:
        answer=input("please enter yes or no:").lower().strip()
        if answer in ("yes","no"):
            print("Congratulations, you know how to follow instructions!")
            break

userInputFunc()