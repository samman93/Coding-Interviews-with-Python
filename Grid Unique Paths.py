import math
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
        c = A - 1
        d = B - 1

		if(B == 1 or A == 1):
			return 1

        return int(math.factorial(c+d)/(math.factorial(c) * math.factorial(d)))

#got the equation from the book. I will try to find the other solution. 
