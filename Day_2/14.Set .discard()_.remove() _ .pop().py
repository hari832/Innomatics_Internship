n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    x = input()
    temp = x.split(" ")
    if temp[0]=='remove':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
    elif temp[0]=='discard':
        if int(temp[1]) in s:
            s.discard(int(temp[1]))
    elif temp[0]=='pop':
        s.pop()


print(sum(s))
