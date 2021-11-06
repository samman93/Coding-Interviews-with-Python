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

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
		grid = []
		for _ in range(A):
			grid.append([0] * B)
		
		for j in range(B):
			grid[A - 1][j] = 1
		for i in range(A): 
			grid[i][B - 1] = 1
		
		for i in range(A - 2, -1 , -1):
			for j in range(B - 2, - 1 , -1):
				grid[i][j] = grid[i][j + 1] + grid [i+1] [j]
 
		return grid[0][0]
#followed along with class
