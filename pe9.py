"""
Project Euler Problem #9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution approach:
a+b+c = n and a < b < c
Thus, a < n/3 and b < n/2 follows
a^2 + b^2 = c^2 ... [1]

a + b = n - c
=> a^2 + b^2 + 2ab = c^2 + 2ab
=> (a+b)^2 = c^2 + 2ab
=> 2ab = (n-c)^2 - c^2 ... [2]

[1] - [2]
=> (b-a)^2 = c^2 - (n-c)^2 - c^2
=> (b-a)^2 = c^2 - n^2 + 2nc

Thus, c should satisfy the condition that (c^2 - n^2 + 2nc) is a perfect square. 
This reduces our search space without having to consider a and b
"""

import math


def spcl_pythogorean_triplet(n):
	"""
	Returns a*b*c where a,b,c are Pythagorean triplets satisfying
	(a+b+c) = n and a < b < c
	"""
	for c in range(math.floor(n/3)+1, math.floor(n/2), 1):
		expr = c*c - n*n + 2*n*c

		# Check whether expr = (b-a)^2
		if expr > 0:
			b_minus_a = math.floor(math.sqrt(expr))
			if expr == b_minus_a*b_minus_a:
				b = (n - c + b_minus_a)//2
				a = n - c - b
				print("a = ", a, "\nb = ", b, "\nc = ", c)
				return a*b*c	
	return -1


if __name__ == "__main__":
	print(spcl_pythogorean_triplet(1000))


