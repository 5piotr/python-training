#! python3

PASSWORDS = {'email':'qoewirjgwodfbskjdflkn','blog':'sergijwerjnwer349834kj','luggage':'2342130'}

import sys, pyperclip

if len(sys.argv) < 2:
	print('użycie: pw.py [konto] - skopiowanie hasła wskazanego konta')
	sys.exit()
	
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Hasło do konta ' + account + ' zostało skopiowane do schowka')
else:
	print('Nie istnieje konto o nazwie ' + account + '.')
	
input('press enter to continue...')