import requests, sys, time
from colorama import Back, Style, Fore
from colorama import init
import subprocess as sp
init()

def main():
	cls()
	print(Fore.WHITE+'*'*25)
	print('+ '+Fore.CYAN+'Dank Xbox IP Resolver'+Fore.WHITE+' +')
	print('+     '+Fore.CYAN+'Created By Inc'+Fore.WHITE+'    +')
	print('*'*25)

	url = 'https://xboxresolver.com/php/Resolve.php'

	user = raw_input(Fore.RED+'Please Enter A Xbox Gamertag: '+Fore.GREEN)
	value = {'name': user}
	r = requests.post(url, data=value)
	print(Fore.MAGENTA+r.content)

	retry = raw_input(Fore.RED+'Would You Like To Resolve Another GT? (Y/n): '+Fore.GREEN)

	if retry == 'y' or retry == 'Y':
		main()
	elif retry == 'n' or retry == 'N':
		Exit()
	elif retry == '':
		print(Fore.YELLOW+'Please Only Type (Y/y) or (N/n)!')

def cls():
	sp.call('clear', shell=True)

def Exit():
	sys.exit('Script Is Shutting Down!\nThanks ~Inc')

if __name__ == '__main__':
	main()
