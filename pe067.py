"""
Project Euler Problem #67: 
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

	3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, 
as there are 2^99 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)

Solution approach:
(Using the exact same logic as #18 since we used DP optimal approach)
We will use dynamic programming approach, going from bottom row to top.  
For every cell, there are two predecessors, we will take the maximum of the two.
The solution will then be the topmost element.
"""


def max_path_sum(t):
	"""
	Find the maximum sum from top to bottom of the triangle
	"""
	for i in range(len(t)-2, -1, -1):
		for j in range(i+1):
			t[i][j] += max(t[i+1][j], t[i+1][j+1])
	return t[0][0]


if __name__ == "__main__":
	f = open("p067_triangle.txt", "r")
	t = f.read()
	triangle = [x.split(" ") for x in t.split("\n")]
	triangle = [list(map(int,i)) for i in triangle]
	print(max_path_sum(triangle))
