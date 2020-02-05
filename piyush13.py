
for n in range(100,9999):
	m=n
	t=n

	s=0
	a=0
	while n>0:
		n=n//10
		a=a+1
	while m>0:
		r=m%10
		m=m//10
		s=s+r**a
	if s==t:
		print("😜:-)s:-)")
	
