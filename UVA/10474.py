#Problem 10474 - Where is the Marble?

def searchA(a, l , r, x):
	if (l > r):
		return -1
	mid = int((l + r) / 2)
	if (a[mid] == x):
		return mid
	else:
		if (a[mid] > x):
			r = mid - 1
			return searchA(a,l,r,x)
		else:
			l = mid + 1
			return searchA(a,l,r,x)

def binarySearch(a, x):
	idx = searchA(a,0,len(a)-1,x)
	return idx
	
	
case = 0


while (1):

	n , q = map(int,input().split())
	
	if (n == 0 and q == 0):
		break
	case = case + 1
	a = []
	for i in range(n):
		x = int(input())
		a.append(x)
		
	a = sorted(a)
	res = []
	qval = []
	for i in range(q):
		
			
		x = int(input())
		
		idx = binarySearch(a,x)
		
		res.append(idx)
		qval.append(x)
		
	print('CASE# {0}:'.format(case))
	for i in range(q):
		x = qval[i]
		idx = res[i]
		if (idx>-1):
			pos = idx
			while (a[pos] == x ):
				pos = pos - 1
				if pos == -1:
					break
			
			idx = pos + 1
			print('{0} found at {1}'.format(x,idx+1))
		else:
			print('{0} not found'.format(x))
		
	