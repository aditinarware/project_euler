"""
Project Euler Problem #6: Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution approach:
1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6
1 + 2 + ... + n = n(n+1)/2
required difference:
n^2*(n+1)^2/4 - n(n+1)(2n+1)/6
= (n-1)n(n+1)(3n+2)/12
"""


def sum_square_difference(n):
	"""
	Returns difference between the sum of the squares of the first n natural numbers and the square of the sum.
	"""
	difference = (n-1)*(n)*(n+1)*(3*n+2)/12
	return difference


if __name__ == "__main__":
	print(sum_square_difference(100))
