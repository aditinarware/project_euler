"""
Project Euler Problem #10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
from common_utils import generate_primes_less_than_n

def sum_of_primes_till_n(n):
	"""
	Calculates the sum of prime numbers below n
	"""
	return sum(generate_primes_less_than_n(n))


if __name__ == "__main__":
	s = time.time()
	print(sum_of_primes_till_n(2000000))
	print("Time taken: ", time.time()-s)
