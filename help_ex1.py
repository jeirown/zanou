#1st Lesson exercise
#find and print the sum of the multiples of 3 less than 1000

#Implementation 1. Using the range function
sum_1 = 0 #initialize sum
for i in range(3,1000,3): #i values: 3,6,9,...,999
	sum_1 += i

print "Implementation 1 - Sum =", sum_1

#Implementation 2. Using the % operator (modulo)
sum_2 = 0 #initialize sum
for i in range(1000): # i values: 0,1,2,...,999
	if i % 3 = 0: #if i is a multiple of 3, add it to the sum. Ignore otherwise
		sum_2 += i

print "Implementation 2 - Sum =",sum_2
#Check validity of both implementations
if sum_1 != sum_2:
	print "Some mistake has been made"
else:
	print "All good"
