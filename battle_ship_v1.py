location = [1, 2, 3]

isSunk = False
guesses = 0
hits = 0

while isSunk == False:
	guess = int(input("Ready!Shoot!(Enter number 0-6)"))
	if guess > 6 or guess < 0:
		print("Please Enter Number 0-6.")
	else:
		guesses += 1
		if guess in location:
			print("HIT!")
			hits += 1
			if hits == 3:
				isSunk = True
				print("You sank my battleship!")
		else:
			print("MISS!")

print("You guessed " + str(guesses) + " times to sink the battleship!")