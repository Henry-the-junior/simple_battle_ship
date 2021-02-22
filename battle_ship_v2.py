location = [1, 2, 3]

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
	guess = int(input("Ready!Shoot!(Enter number 0-6)"))
	if guess > 6 or guess < 0:
		print("Please Enter Number 0-6.")
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