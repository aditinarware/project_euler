"""
Project Euler Problem #19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

months = [31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap_year(year):
	""" 
	Test whether the given 'year' is a leap-year
	"""
	return ((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0))


def counting_sundays():
	day = 1 # Monday
	sunday_count = 0

	# Finding the first day of 1901 (1 Jan 1901)
	for year in range(1900,1901):
		for m in months:
			day += m
			if is_leap_year(year) and m == 28:
				day += 1

	for year in range(1901,2001):
		for m in months:
			day += m
			if is_leap_year(year) and m == 28:
				day += 1
			if day % 7 == 0:
				sunday_count += 1

	return sunday_count


if __name__ == "__main__":
	print (counting_sundays())
