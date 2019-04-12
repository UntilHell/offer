#list = [2,4,5,8,4,9,7]
#min = list[0]
#max = list[0]
#for x in list:
#	if x > max:
#		max = x
#	if x < min:
#		min = x
#print (min,max)

def findMinAndMax(L):
	if L == []:
		return (None,None)
	else:
		min = L[0]
		max = L[0]
	for n in L:
		if min > n:
			min = n
		if max < n:
			max = n
	return (min,max)
	
	
	
l = [1,8,9,4,6,3,0]
print(findMinAndMax(l))