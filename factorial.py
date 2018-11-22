factorial=[]
print("Enter a number: ")
start_num = input()
current_num=1
int(start_num)

while start_num > 0:
    factorial.append(start_num)
    start_num=start_num-1

for i in factorial:
    current_num=current_num * int(i)

print(factorial)
print(current_num)

