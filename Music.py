import random
from playsound import playsound
while True:
	a = random.randrange(1, 6)
	if 1 == a:
		print("Playing warbringer")
		playsound('war.mp3')
	if 2 == a:
		print("Playing egg")
		playsound('Egg.mp3')
	if 3 == a:
		print("Playing Fire") 
		playsound('Fire.mp3')
	if 4 == a: 
		print("Playing MOAI")
		playsound('MOAI.mp3')
	if 5 == a: 
		print("Playing spooky")
		playsound('spooky.mp3')
	if 6 == a: 
		print("Playing Terraria")
		playsound('Terraria.mp3')