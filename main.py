from BubbleSort import *
from QuickSort import *
from time import time
from random import randint as random

times = []

for l in range(100,1001,100):
	lists = [[random(0,l) for i in range(l)] for j in range(100)]
	bubbleStart = time()
	for dataset in lists:
		bubbleSort(dataset)
	bubbleEnd = time()
	bubbleTime = bubbleEnd - bubbleStart
	quickStart = time()
	for dataset in lists:
		quickSort(dataset)
	quickEnd = time()
	quickTime = quickEnd - quickStart
	print([bubbleTime,quickTime])