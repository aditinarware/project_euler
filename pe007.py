"""
Project Euler Problem #7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math
import time


def nth_prime(n):
	"""
	Returns the nth prime number
	"""
	list_of_primes = [2]
	count = 1
	prime_candidate = 3

	while(count < n):
		is_prime = True
		sqrt_prime_candidate = math.sqrt(prime_candidate)
		for i in list_of_primes:
			if prime_candidate%i == 0:
				is_prime = False
				break
			if i > sqrt_prime_candidate:
				break
		if is_prime:
			list_of_primes.append(prime_candidate)
			count += 1
		prime_candidate += 2		
	return list_of_primes[-1]


if __name__ == "__main__":
	s = time.time()
	print(nth_prime(10001))
	print("Time taken: ", time.time()-s)
