"""
Project Euler Problem #20: Factorial digit sum
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial
from common_utils import digits_sum


def factorial_digits_sum(n):
	"""
	Returns the sum of the digits of n!
	"""
	return digits_sum(factorial(n))


if __name__ == "__main__":
	print(factorial_digits_sum(100))
