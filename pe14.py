"""
Project Euler Problem #14: Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

length_dict = {1:1}

def chain_length(n):
	"""
	Computes the lenght of Collatz sequence starting at n. 
	We cache the result in the dictionary to avoid re-computing the tail.
	"""
	try:
		return length_dict[n]
	except KeyError:
		if n%2 == 0:
			length_dict[n] = 1 + chain_length(n//2)
		else:
			length_dict[n] = 1 + chain_length(3*n+1)
		return length_dict[n]


def max_chain_length(upper_limit):
	"""
	Returns the starting number under upper_limit which produces the longest chain
	"""
	max_length = 0
	ans = 0
	for i in range(1, upper_limit):
		c = chain_length(i)
		if c > max_length:
			max_length = c
			ans = i
	return ans


if __name__ == "__main__":
	print(max_chain_length(1000000))
