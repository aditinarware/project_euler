"""
Project Euler Problem #15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Solution approach:
Any sequence of 20 D's (down) and 20 R's (right) will be a valid route.
Total number of ways to arrange 20 D's and 20 R's = (40C20)
"""


def lattice_paths(n):
	"""
	Returns the number of paths for a nxn grid
	"""
	ans = 1
	# We are computing 2nCn
	for i in range(1,n+1):
		ans *= (n+i)
	for i in range(1,n+1):
		ans //= i	
	return ans


if __name__ == "__main__":
	print(lattice_paths(20))
