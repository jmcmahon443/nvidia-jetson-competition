#! /env/bin/python
import sys


				
if len(sys.argv) == 2:

	x=0
	print("you can also specify the timestamp for the initila  beat")

elif len(sys.argv) == 3:

	x=float(sys.argv[2]) 
	
else:
	sys.exit("specify the output file name")
	
	
intervals=[]
n=int(raw_input("How many beats are hit in your bar?"))
print("Enter intervals one by one:")
for i in range(n):
	intervals.append(float(raw_input()))

fh = open(sys.argv[1], "w")
	#arr is the created array, intervals is the increment of each element in the pattern 
N=len(intervals)

#initial
arr=[x]
fh.write(str(x)+"\n")	

for a in range(1,200):
	for i in range (N):
		if a%N==i:
			new=arr[a-1] + intervals[i]
			arr.append(new)#increment the prvious value
			break #done with the nested loop if found
	fh.write(str(new)+"\n")

fh.close()



			

	
