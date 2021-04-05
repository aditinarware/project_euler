"""
Project Euler Problem #17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

# proper names
proper = [
  0, len("one"), len("two"),len("three"), len("four"), len("five"), 
  len("six"), len("seven"), len("eight"), len("nine"),len("ten"), 
  len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), 
  len("sixteen"), len("seventeen"), len("eighteen"), len("nineteen")
]
# prefixes for tenth place
tenth = [
  None, None, len("twenty"), len("thirty"), len("forty"), len("fifty"),
  len("sixty"), len("seventy"), len("eighty"), len("ninety")
]


def find_len_below_100(n):
	"""
	Returns the length of the name for n below 100
	"""
	if n < 20:
		return proper[n]
	return tenth[n//10] + proper[n%10]


def find_num_len(n):
	"""
	Returns the length of the name for n
	"""
	if n < 100:
		return find_len_below_100(n)

	res = 0
	h = (n // 100) % 10
	t = n // 1000
	s = n % 100

	if n > 999:
		res += find_len_below_100(t) + len("thousand")
	if h != 0:
		res += proper[h] + len("hundred")
	if s != 0:
		res += len("and") + find_len_below_100(s)
	
	return res;


def num_letter_count(n):
	"""
	Returns the total length of words for 1 to n
	"""
	res = 0
	for i in range(n+1):
		res += find_num_len(i)
	return res


if __name__ == "__main__":
	print(num_letter_count(1000))
