from random import shuffle
import time
import numpy as np 

def maxSubSum(vector):
	maxSum=0
	for i in range((len(vector))):

		for j in range(i,len(vector)):
			thisSum=0
			for k in range (i,j):
				thisSum=thisSum+vector[k]
			if (thisSum>maxSum):
				maxSum=thisSum
	return maxSum


array = np.arange(1000)
shuffle(array)
starttime = time.time()
print(maxSubSum1(array))
endtime = time.time() 
print (endtime-starttime)
