# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
sumTotal = 0

for i in range (1, 1000, 1):
	if i % 3 == 0:
		sumTotal = sumTotal + i
		# print '3 %s' % i
	elif i % 5 == 0:
		sumTotal = sumTotal + i
		# print "5 %s" % i

print sumTotal

#Answer = 233168 is Correct