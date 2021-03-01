class View:

	def __init__(self, boardSize):
		self.boardSize = boardSize

	def displayBoard(self):
		print("----" * Model.boardSize + "-")
		for row in Model.seaBlock:
			s = ""
			for block in row:
				s += "| " + block + " "
			s += "|"
			print(s)
			print("----" * Model.boardSize + "-")

class Model:

	def __init__(self, boardSize, shipSize, numShips, shipsSunk, ships, seaBlock):
		self.boardSize = boardSize
		self.shipSize = shipSize
		self.numShips = numShips
		self.shipsSunk = shipsSunk
		self.ships = ships
		self.seaBlock = seaBlock

	def fire(self, guess):
		if seaBlock[guess[1]][guess[0]] == " ":
			for ship in self.ships:
				if guess in ship['location']:
					self.seaBlock[guess[1]][guess[0]] = "H"
					ship['hits'][ship['location'].index(guess)] = 1
					if self.isSunk(ship['hits']):
						self.shipsSunk += 1
					break
				else:
					self.seaBlock[guess[1]][guess[0]] = "M"
		else:
			print("You've fired this block.")

	def isSunk(self, hits):
		for hit in hits:
			if hit == 0:
				return False
		return True

class Controller:

	def __init__(self, guesses):
		self.guesses = guesses

	def processGuess(self, guess):
		if parseGuess(guess):
			Model.fire(parseGuess(guess))
		else:
			pass
		
def parseGuess(guess):

	if len(guess) != 2:
		return False
		
	else:
		try:
			row = int(guess[0])
			col = int(guess[1])
			return (row, col)
		except:
			return False




boardSize = 7

seaBlock = []
for i in range(boardSize):
	seaBlock.append([" "] * boardSize)

shipSize = 3

numShips = 3

shipsSunk = 0

ships = [{"location": [(1, 1), (1, 2), (1, 3)], "hits": [0, 0, 0]}, 
		 {"location": [(5, 3), (5, 4), (5, 5)], "hits": [0, 0, 0]}, 
		 {"location": [(3, 4), (3, 5), (3, 6)], "hits": [0, 0, 0]}]

View = View(boardSize)
Model = Model(boardSize, shipSize, numShips, shipsSunk, ships, seaBlock)

guesses = 0

Controller = Controller(guesses)

while Model.shipsSunk != Model.numShips:
	guess = input("Ready!Shoot!")
	Controller.processGuess(guess)
	#print(Model.ships)
	View.displayBoard()
	print(Model.shipsSunk)

