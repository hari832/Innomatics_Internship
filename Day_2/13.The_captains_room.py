# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=input().split()
x=set()
y=set()
for i in b:
    if i not in x:
        x.add(i)
    else:
        y.add(i)
print(x.difference(y).pop())

        
    
