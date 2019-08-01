x11=int(input())
for o in range(1,x11+1):
	s11=x11//o
	if s11%2==1 and x11%o==0:
		print(o)
		break
