import sys

n = input('Enter length (in measures/bars) of piece: ')
try:
	n = int(n)
	if n < 1:
		print("Invalid input. Number should be at least 1.")
		sys.exit()
except ValueError:
	print("Invalid input. Input should be an integer.")
	sys.exit()

if n > 9:
	ans = input('You entered a number that will require a long compute time.  Are you sure you want to continue? (y/n): ')
	if ans != 'y':
		print('Terminating...')
		sys.exit()

def find_count(num, count):
	if (num > 1):
		if num%8 != 0:
			for i in range(11): 
				count = find_count(num - 1, count ) 
		else:
			for i in range(2): 
				count = find_count(num - 1, count ) 
	else:      
		count += 11
	return count

count = find_count(n, 0)
print('There are a total of {:,} combinations of minuets that can be created'.format(count))