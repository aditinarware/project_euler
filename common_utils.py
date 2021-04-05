"""
Contains some common utililty functions
"""

import math


def generate_primes_less_than_n(n):
	"""
	Returns a list of prime numbers which are less than n
	"""
	if n <= 1:
		return []

	list_of_primes = [2]
	prime_candidate = 3

	while(prime_candidate < n):
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
		prime_candidate += 2	

	return list_of_primes


def tau(num):
	"""
	Returns the number of divisors of a natural number 'num' given by tau(n) function.
	n can be expressed as product of primes pi^ei
	Then, the number of divisors = product(ei+1)
	"""
	if num == 1:
		return 1

	n = num
	i = 2 # prime number
	product = 1

	# Check only till the prime numbers less than sqrt of n
	while(i*i <= n):
		exp = 0 # exponent of the prime factor
		while n%i == 0:
			n /= i
			exp += 1
		i += 1
		product *= exp + 1
	
	if n == num or n > 1:
		product *= 1 + 1

	return product


def digits_sum(num):
	"""
	Returns the sum of the digits of num
	"""
	return sum(map(int, str(num)))
