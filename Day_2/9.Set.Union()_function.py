# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
print(len(x|y))
