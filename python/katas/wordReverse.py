#!/usr/bin/python

def main(word):
	
	def invertWord(word):

                invertedWord = word.reverse()
		return invertedWord
	return	invertWord(word)

userInput = raw_input('Give me a word to reverse \n until you hit Q\n')
while userInput!='Q':

	main(userInput)	

	userInput = raw_input('Other word\n')
else:
	pass
