def quickSort(l):
	n = len(l)
	if n <= 1:
		return l
	else:
		lower = []
		equal = []
		higher = []
		pivotValue = l[0]
		for val in l[1:]:
			if val < pivotValue:
				lower.append(val)
			elif val > pivotValue:
				higher.append(val)
			else:
				equal.append(val)
	return quickSort(lower) + equal + [pivotValue] + quickSort(higher)