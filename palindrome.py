#My solution to the problem. Still trying to learn the short way to do things in Python.
#Answer was correct at 906609
prevLen = 0
lrgPal = 0

for x in range (100, 1000, 1):
	for y in range (100, 1000, 1):
		z = x * y
		num = str(z)

		length = len(num)
		temp = length
		i = 0
		while i < length:
			if i == temp - 1:
				break;
			if num[i] == num[temp - 1]:
				flag = "true"
				i = i + 1
				temp = temp - 1
			else:
				flag = "false"
				break
		if flag == "true" and length >= prevLen and z >= lrgPal:
			lrgPal = z
			prevLen = length

print lrgPal



# Found this code online. Way simpler to read and I was able to notice how they flipped the string
# in reverse to check for a palindrome


# print max(x * y
# 	for x in xrange(100,1000)
# 		for y in xrange(100,1000)
# 			if str(x*y) == str(x*y)[::-1])