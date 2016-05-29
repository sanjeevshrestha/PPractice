import random

class Dice:
	"""
	Dice Program to generate random dice roll
	"""

	def __init__(self):
		print "Roll the dice and guess the number"
		print "----------------------------------"

	def roll(self):
		return random.choice([1,2,3,4,5,6])


if __name__=='__main__':
	dice =Dice()
	while True:
		
		try:
			rolled=dice.roll()
			guess=int(raw_input("Guess a number: "))
			if(guess==rolled):
				print "You guessed it right. The rolled number is %d" %guess
			else:
				print "Your guess was wrong. The rolled number is %d" %rolled

			print "====================================="
			opt=raw_input("Do you want to continue? (y/n): ")
			if(opt.lower()=='n'):
				break

		except ValueError:
			print "Oops! does not look like a valid input"
	
		
