"""
Project Euler Problem #16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from common_utils import digits_sum


def power_digit_sum(base, power):
	"""
	Returns the sum of digits of base^power
	"""
	num = base**power
	return digits_sum(num)


if __name__ == "__main__":
	print(power_digit_sum(2,1000))
