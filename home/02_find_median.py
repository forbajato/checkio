# Note - this will work for Python 2.7, for Python 3 you seem to need to make the list indices integers rather than floats.
def median(l):
	l.sort()
	if len(l) % 2 == 1:
		return l[len(l)/2]
	else:
		return (l[len(l)/2]+l[len(l)/2 -1])/2.0

#Python 3 version:
#def median(l):
	#l.sort()
	#if len(l) % 2 == 1:
		#return l[int(len(l)/2)]
	#else:
		#return (l[(len(l)/2)]+l[int(len(l)/2 -1)])/2.0


