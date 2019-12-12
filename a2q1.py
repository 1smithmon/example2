from SimpleGraphics import *
import random

numberH = 1
numberC = 1

# human’s label
rect(100, 100, 250, 50)
setFont("Arial", "30", "bold")
text(225, 125, "HUMAN")

# computer’s label
rect(450, 100, 250, 50)
text(575, 125, "COMPUTER")

# layout for human’s board
for y in range (200, 450, 50):
	for x in range(100, 350, 50):
		rect(x, y, 50, 50)
		text(x + 25, y + 25, numberH)
		numberH = numberH + 1

# layout for computer’s board
for y in range (200, 450, 50):
	for x in range(450, 700, 50):
		rect(x, y, 50, 50)
		text(x + 25, y + 25, numberC)
		numberC = numberC + 1
# human’s ship
humanS = int(input("Select centre number for your ship: "))
while humanS == 1 or humanS == 6 or humanS == 11 or humanS == 16 or humanS == 21 or \
humanS == 5 or humanS == 10 or humanS == 15 or humanS == 20 or humanS == 25 or \
humanS > 25 or humanS < 1:
	humanS = int(input("That is not a valid place. Try again: "))

# computer’s ship
computerS = random.randint(1,25)
while computerS == 1 or computerS == 6 or computerS == 11 or computerS == 16 or \
computerS == 21 or computerS == 5 or computerS == 10 or computerS == 15 or \
computerS == 20 or computerS == 25:
	computerS = random.randint(1,25)

# creating variables for the place of ship
x = 50
y = 200
l = 50

# placing human’s ship
setFill(255, 192, 192)
humanP1 = rect(x + (humanS % 5 - 1) * 50, y + (humanS // 5) * 50, l, l)
humanP2 = rect(x + humanS % 5 * 50, y + (humanS // 5) * 50, l, l)
humanP3 = rect(x + (humanS % 5 + 1) * 50, y + (humanS // 5) * 50, l, l)

# changing variable values
m = 400
n = 200

# placing computer’s ship (invisible)
setFill(None)
computerP1 = rect(m + (computerS % 5 - 1) * 50, n + (computerS // 5) * 50, l, l)
computerP2 = rect(m + computerS % 5 * 50, n + (computerS // 5) * 50, l, l)
computerP3 = rect(m + (computerS % 5 + 1) * 50, n + (computerS // 5) * 50, l, l)

text(x + (computerS % 5 - 1) * 50 + 25, y + (computerS // 5) * 50 + 25, computerS - 1)
text(x + computerS % 5 * 50 + 25, y + (computerS // 5) * 50 + 25, computerS)
text(x + (computerS % 5 + 1) * 50 + 25, y + (computerS // 5) * 50 + 25, computerS + 1)

# setting boolean variables for human and computer hits
hH1 = False
hH2 = False
hH3 = False
cH1 = False
cH2 = False
cH3 = False
setFill(100, 100, 200)
cGuess = random.randint(1,25)

while (hH1 == False or hH2 == False or hH3 == False) and \
(cH1 == False or cH2 == False or cH3 == False):
	hGuess = int(input("Select a number to fire upon: "))
	cGuess = random.randint(1,25)
	setFill(100, 100, 200)
	if hGuess == computerS - 1:
		print("HIT!")
		setFill(0, 200, 100)
		rect(m + (computerS % 5 - 1) * 50, n + (computerS // 5) * 50, l, l)
		cH1 = True
	elif hGuess == computerS:
		print("HIT!")
		setFill(0, 200, 100)
		rect(m + computerS % 5 * 50, n + (computerS // 5) * 50, l, l)
		cH2 = True
	elif hGuess == computerS + 1:
		print("HIT!")
		setFill(0, 200, 100)
		rect(m + (computerS % 5 + 1) * 50, n + (computerS // 5) * 50, l, l)
		cH3 = True
	else:
		setFill(250, 50, 100)
		print("MISS!")
		if hGuess % 5 == 0:
			rect(m + ((hGuess - 1) % 5 + 1) * 50, n + (hGuess // 5) * 50 - 50, l, l)
		else:
			rect(m + ((hGuess - 1) % 5 + 1) * 50, n + (hGuess // 5) * 50, l, l)
	if cGuess == humanS - 1:
		print("The computer HIT!")
		setFill(0, 200, 100)
		rect(x + (humanS % 5 - 1) * 50, y + (humanS // 5) * 50, l, l)
		hH1 = True
	elif cGuess == humanS:
		print("The computer HIT!")
		setFill(0, 200, 100)
		rect(x + humanS % 5 * 50, y + (humanS // 5) * 50, l, l)
		hH2 = True
	elif cGuess == humanS + 1:
		print("The computer HIT!")
		setFill(0, 200, 100)
		rect(x + (humanS % 5 + 1) * 50, y + (humanS // 5) * 50, l, l)
		hH3 = True
	else:
		setFill(250, 50, 100)
		print("The computer MISSES!")
		if cGuess % 5 == 0:
			rect(x + ((cGuess - 1) % 5 + 1) * 50, y + (cGuess // 5) * 50 - 50, l, l)
		else:
			rect(x + ((cGuess - 1) % 5 + 1) * 50, y + (cGuess // 5) * 50, l, l)
if hH1 == True and hH2 == True and hH3 == True:
	print("Your ship was sunk")
else:
	print("Congratulations. You sunk the opponent’s ship")


# Collier, R. "Lectures Notes for COMP1005B - Introduction to Computer Science I"
# [PDF documents]. Retrieved from cuLearn: https://www.carleton.ca/culearn/
# (Winter 2016).