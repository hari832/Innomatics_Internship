# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
A=set(map(int,input().split()))
n= int(input())
for i in range(n):
    func,val=input().split()
    B=set(map(int,input().split()))
    eval('A.{}({})'.format(func,B))
    
print(sum(A))
