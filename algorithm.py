import sys
import math

n = input('Enter length (in measures/bars) of piece: ')
try:
	n = int(n)
	if n < 1:
		print("Invalid input. Number should be at least 1.")
		sys.exit()
except ValueError:
	print("Invalid input. Input should be an integer.")
	sys.exit()

exp = math.floor(n/8)
count = (2**exp) * (11**(n-exp))
print('There are a total of {:,} combinations of minuets that can be created'.format(count))