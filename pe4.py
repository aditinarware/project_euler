"""
Project Euler Problem #4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Solution approach:
The largest number would be 6-digits: abccba = p*q
p * q = 100000*a + 10000*b + 1000*c + 100*c + 10*b + 1*a
p * q = 100001*a + 10010*b + 1100*c
p * q = 11*(9091*a + 910*b + 100*c)
Thus, either p or q must be divisible by 11
"""

def is_palindrome(num):
	"""
	Checks if a given number is a palindrome
	"""
	s = str(num)
	return s == s[::-1]


def largest_palindrome():
	"""
	Finds the largest palindrome which is product of two 3-digit numbers
	"""
	result = 0
	for i in range(990, 100, -11):
		for j in range(999, 100, -1):
			product = i*j
			if product > result and is_palindrome(product):
				result = product
				break
			# p*q = q*p. So if we get to a point where our product is less than the result,
			# we can skip checking any smaller numbers that would come after that on the inner loop.
			elif result > product:
				break
	return result


if __name__ == "__main__":
	print(largest_palindrome())
