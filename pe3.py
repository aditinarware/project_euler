"""
Project Euler Problem #3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def largest_prime_factor(n):
	"""
	Finds the largest prime factor of a given number
	"""
	maxPrime = -1
    
	# Keep dividing n by 2 to get rid of all the even composite factors.
	while n % 2 == 0: 
		maxPrime = 2
		n >>= 1 # equivalent to n //= 2

	# Loop over the possible odd factors to remove the rest of the composites, 
	# and updating maxPrime to the largest factor.
	for i in range(3, int(math.sqrt(n)) + 1, 2): 
		while n % i == 0: 
			maxPrime = i 
			n //= i 

	# If n > 2 then n must be prime so we return it, otherwise we return maxPrime
	return n if n > 2 else maxPrime


if __name__ == "__main__":
	print(largest_prime_factor(600851475143))
