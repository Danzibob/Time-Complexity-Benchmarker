def bubbleSort(l):
	n = len(l)
	swapped = True
	while swapped:
		swapped = False
		for i in range(1,n):
			if l[i-1] > l[i]:
				l[i],l[i-1] = l[i-1:i+1]
				swapped = True
	return l
