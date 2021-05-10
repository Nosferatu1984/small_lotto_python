import random
import time

number = random.randint(1, 10)

for i in range(3):
	print("Try ", i + 1)
	odp = input("Try to guess number 0-10? ")

	if number == int(odp):
		print("You guess it!")
		break
	elif i == 2:
		print("I think about: ", number)
	else:
		print("Its bad answer")

time.sleep(15)
