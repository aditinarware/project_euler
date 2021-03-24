"""
Project Euler Problem #2: Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def even_fib(max_limit):
	"""
	Generates even valued fibonacci term less than the max_limit
	"""
	a, b = 1, 2
	while a < max_limit:
		if not a%2:
			yield a
		a, b = b, a + b


if __name__ == "__main__":
	print(sum(even_fib(4000000)))
