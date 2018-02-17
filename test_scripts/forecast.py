#! bin/python

import sys
import numpy as np

data = open("../output/test")
beats=[float(ln) for ln in data.readlines()]
normalized = np.subtract(beats,beats[0])
#print(0, beats[0]," ")
#presum=np.sum(normalized[:i])
presum=0
I=0
e=0
e_sum=0
print(0, "	",beats[0], "  ", "-", "  ", "-")
for i in range(1,len(beats)-1): #care elemnt number vs index
	I+=i
	presum+=normalized[i-1]
	next=(presum/I)*(i+1)+beats[0]
	adjusted_next=((presum-e_sum)/(I+e))*(i+1)
	e=adjusted_next-beats[i]
	e_sum+=e
	
	print(i, "	", beats[i], "	", next, "	", adjusted_next, "	", e)
	#print(beats[i]-beats[i-1])
