#T = (15, "python", 4.00, [2, 3, 4, 5], (4, 5, 6, 7), 4+2j)
#print(T)

T = ()
k = int(input())
for i in range(k):
   d = input()
   if d.isalpha():
       T+=(d,)
   else:
       T+=(eval(d),)

print(T)
