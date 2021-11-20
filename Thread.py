from threading import Thread
import os
from playsound import playsound
import random
import time
import webbrowser
def Song():
	a = random.randrange(1, 6)
	e = input("Website tool (y/n): ")
	if e == 'y':
		print("Using a website tool...")
		time.sleep(0.1)
		YourMomsWeightInTons = int(input("""
anonboot (1)
vtoxicity (2)
instant-stresser (3)
deltastress (4):
"""))
		if YourMomsWeightInTons == 1:
			print("Opening anonboot")
			webbrowser.open("https://anonboot.com/login.php")
		if YourMomsWeightInTons == 2:
			print("Opening vtoxicity")
			webbrowser.open("https://vtoxicity.net/login")
		if YourMomsWeightInTons == 3:
			print("Opening instant-stresser")
			webbrowser.open("https://instant-stresser.com/hub")
		if YourMomsWeightInTons == 4:
			print("Opening deltastress")
			webbrowser.open("https://deltastress.com/login")
		time.sleep(1)
		playsound('ThankYou.mp3')
		
	if e == 'n':
		print("You chose coded tool...")
		time.sleep(0.1)
		Layer = int(input("Layer 7 (7), layer 4 (4), or layer 3 (3): "))
		if Layer == 3:
			print("You chose L3 (Old ip attack)")
			time.sleep(1)
			print("Using 'POD'")
			time.sleep(0.5)
			os.system("python3 POD.py")
		if Layer == 4:
			print("You chose L4 (ip)")
			time.sleep(0.1)
			print("Using 'TCP-UDP-Flood")
			time.sleep(0.1)
			os.system("python3 flood.py")
		if Layer == 7:
			print("You chose L7 (website)")
			time.sleep(0.1)
			print("Using 'pyflooder'")
			time.sleep(0.1)
			website = input("Website: ")
			port = input("Port: ")
			attacks = input("Attacks: ")
			playsound('attack.mp3')
			os.system("python3 pyflooder.py " + website + " " + port + " " + attacks)
			playsound('ThankYou.mp3')



def Song2():
	while True:
		a = random.randrange(1, 6)
		if 1 == a:
			playsound('war.mp3')
		if 2 == a:
			playsound('Egg.mp3')
		if 3 == a: 
			playsound('Fire.mp3')
		if 4 == a: 
			playsound('MOAI.mp3')
		if 5 == a: 
			playsound('spooky.mp3')
		if 6 == a: 
			playsound('Terraria.mp3')
Thread(target = Song).start() 
Thread(target = Song2).start()