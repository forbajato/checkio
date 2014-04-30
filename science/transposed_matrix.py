#!/usr/bin/env python

def checkio(data):
    #replace this for solution
	 data_prime = [] #transformed matrix
	 temp_list = []
	 for i in data:
		 temp_list.append(i.pop(0)) #This will get the first item in each element list and put them into a temporary list.
	 data_prime.append(temp_list)

	 #These "asserts" using only for self-checking and not necessary for auto-testing
	 if __name__ == '__main__':
	     assert checkio([[1, 2, 3],
		                  [4, 5, 6],
		                  [7, 8, 9]]) == [[1, 4, 7],
		                                  [2, 5, 8],
		                                  [3, 6, 9]], "Square matrix"
		  assert checkio([[1, 4, 3],
		                  [8, 2, 6],
		                  [7, 8, 3],
		                  [4, 9, 6],
		                  [7, 8, 1]]) == [[1, 8, 7, 4, 7],
		                                  [4, 2, 8, 9, 8],
		                                  [3, 6, 3, 6, 1]], "Rectangle matrix"

