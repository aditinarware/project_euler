"""
Project Euler Problem #5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution approach:
Let the required number be N which is divisible by all numbers from 1 to k
N = p1^a1 * p2^a2 *... where pi is the ith prime number less than or equal to k
ai is the largest number such that pi^ai <= k
Thus, ai = Floor(log(k)/log(pi))
"""

import math


def generate_prime_less_than_n(n):
	"""
	Returns a list of prime number less than or equal to the given number 'n'
	"""
	if n <= 1:
		return []
	list_of_primes = [2]
	for i in range(3, n, 2):
		is_prime = True
		for j in list_of_primes:
			if i%j == 0:
				is_prime = False
				break
		if is_prime:
			list_of_primes.append(i)
	return list_of_primes


def smallest_number_divisible(n):
	"""
	Returns the smallest positive number divisible by all the numbers from 1 to n
	"""
	prime_numbers = generate_prime_less_than_n(n)
	log_n = math.log(n)
	res = 1
	for pi in prime_numbers:
		res *= math.pow(pi, math.floor(log_n/math.log(pi)))
	return res


if __name__ == "__main__":
	print(smallest_number_divisible(20))
