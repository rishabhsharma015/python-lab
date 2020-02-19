T = tuple(map(str,input().split()))
b = []
for i in T:
    if T.count(i)>1:
       print(i)
       b.append(i)
print(b)
