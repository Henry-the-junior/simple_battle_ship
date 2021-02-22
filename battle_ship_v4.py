import random

loc = random.randint(0, 4)

location = [loc, loc + 1, loc + 2]

isSunk = False
guesses = 0
hits = 0

status = [' '] * 7

def view(status):
	print("-" * 29)
	print("|", status[0],
		  "|", status[1],
		  "|", status[2],
		  "|", status[3],
		  "|", status[4],
		  "|", status[5],
		  "|", status[6], "|")
	print("-" * 29)

while isSunk == False:
	view(status)
	guess = input("Ready!Shoot!(Enter number 0-6)")
	try:
		guess = int(guess)
	except:
		print("Please Enter Number 0-6.")
		continue
	if guess not in [0, 1, 2, 3, 4, 5, 6]:
		print("Please Enter Number 0-6.")
	if status[guess] == "H" or status[guess] == "M":
		print("You've tried this position, Please Enter Again.")
	else:
		guesses += 1
		if guess in location:
			print("HIT!")
			status[guess] = "H"
			hits += 1
			if hits == 3:
				isSunk = True
				view(status)
				print("You sank my battleship!")
		else:
			status[guess] = "M"
			print("MISS!")

print("You guessed " + str(guesses) + " times to sink the battleship!")