fib_series=[1,1]
print("Enter to amount of fibonacci series you want to iterate through:")
fib_count=input()
fib_count-=2
i=0
while i < fib_count:
    current_num=fib_series[-1]+fib_series[-2]
    fib_series.append(current_num)
    i+=1
print(fib_series)
count=1

for x in range(0,len(fib_series)):
    print(str(count)+" = "+str(fib_series[x]))
    count+=1
