#! /usr/bin/env python

"""Still on the Home island.

The task is to process a piece of text of arbitrary length.  You want to find the most frequent letter in the text.  Upper and lower case count as the same ("A" and "a" are both the same) but the returned value must be a lower case letter.  If the text has no repeats then return the letter earliest in the alphabet.

Examples:

	checkio("Hello World!") == "l"
	checkio("How do you do?") == "o"
	checkio("One") == "e"
	checkio("Oops!") == "o"
	checkio("AAaooo!!!!") == "a"
	checkio("abe") == "a"

"""
def checkio(text):
    #replace this for solution
    chars = {}
	 #Count the characters
    for character in text:
        character = character.lower() #Make it lower case
        if character.isalpha(): #Make sure it is a character and not punctuation
            chars[character] = chars.get(character,0)+1
    for k,v in chars.iteritems(): #look through the dictionary for the highest value and return the key associated with it
        if v == max(chars.values()):
            return k

'''def better(text):
	text = ''.join(i for i in text.lower if i.isalpha())
	return max(set(text),key=text.count)
	%From alaf's solution
'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
