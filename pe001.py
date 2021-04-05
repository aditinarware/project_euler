"""
Project Euler Problem #1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def sum(n, k):
	"""
	Returns sum of multiples of k which are less than n
	"""
	d = n // k
	return k * (d * (d+1)) // 2

  
def sum_of_multiples(n):
	"""
	Returns sum of all multiples of 3 or 5 below n
	"""
	return sum(n-1, 3) + sum(n-1, 5) - sum(n-1, 15)


if __name__ == "__main__":
	print(sum_of_multiples(1000))
