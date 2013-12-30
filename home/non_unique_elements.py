#! /usr/bin/env python

''' The non-unique-elements puzzle seems to be the place to start.  When you click on it you get a youtube video on using the interface to write, check an submit your code.

The puzzle is to take a list with an arbitrary number of elements and return a list of only those elements that are repeated.  This is somewhat like the puzzle in the Python Challenge with a huge block of text from which you are to find the unique elements but done backwards.  My attempts are below.  The first one passed.
'''

def checkio(data):
	'''While this has the benefit of working it is inelegant, perhaps a list comprehension will be better.'''
	ans = []
	for r in data:
		if data.count(r) > 1:
			ans.append(r)
	return ans

def checkio_list_comprehension(data):
	''' List comprehensions can have conditionals!'''
	ans = [r for r in data if data.count(r) > 1]
	return ans


