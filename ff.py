import json,re,sys,os,time
from time import sleep
try:
	import requests
	from bs4 import BeautifulSoup
except:
	print ("\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4")
	sys.exit()

c = requests.Session()

with open('cookies.json', 'r') as myfile:
      data = myfile.read()
# parse file
obj = json.loads(data)

def teks(wkwk):
    for haha in wkwk + '\n':
        sys.stdout.write(haha)
        sys.stdout.flush()
        time.sleep(0.0045)


banner = """\033[0;35m    ____  __  ______  __  ___    __
   / __ \/ / / / __ \/ / / / |  / /
  / / / / /_/ / /_/ / / / /| | / / 
 / /_/ / __  / _, _/ /_/ / | |/ /  
/_____/_/ /_/_/ |_|\____/  |___/   
\033[0;34m=========================================================
\033[1;32mAuthor By  \033[1;31m :\033[1;0m DHRUV
\033[1;32mChannel Yt\033[1;31m  : \033[1;0mDhruv
\033[1;32mWhich Web \033[1;31m  :\033[1;0m Ad LTC¤ï¸"""
os.system("clear")
teks(banner)
try:
	import colorama
	from colorama import Fore, Back, Style
	from random import randint
	from datetime import datetime
	colorama.init(autoreset=True)
except:
	print("\033[1;30m# \033[1;31mTo install Please Type pip install colorama")

#timer
def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                         ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)

#animation

green = Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
white2 = Style.NORMAL+Fore.WHITE
purple = Style.NORMAL+Fore.MAGENTA
green2 = Style.NORMAL+Fore.GREEN
red2 = Style.NORMAL+Fore.RED
red = Style.BRIGHT+Fore.RED

ua = {
 "Host": "adltc.cc",
 "user-agent": obj['User-Agent'],
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8,de;q=0.7,id;q=0.6",
 "cookie": obj['Cookies'],
 "referer": "https://adltc.cc/surf"
}

try:
	h = c.get("https://www.google.com/")
except:
	print(red2+"please check your internet or off you vpn")
	sys.exit()
sys.stdout.write("\n")
while True:
	try:
		resp = c.get("https://adltc.cc/surf", headers=ua)
		soup = BeautifulSoup(resp.content, 'html.parser')
		sss = (resp.text)
	except:
		print(red2+"please Update Your Cookies")
		sys.exit()
		pass
	
	try:
		bal = soup.find_all("div", class_="card-panel light-blue darken-4 center")[0]
		bal = bal.find_all("p", class_="white-text flow-text")[0]
		bal = bal.find_all("b")[0].text #replace(" LTC", "")
	except:
		sys.stdout.write("\r")
		sys.stdout.write("\033[1;31mplease Update Your Cookies\n")
		sys.stdout.flush()
		sleep(1)
		sys.exit()
		pass
	
	
	
	try:
		adsid = soup.find_all("input", id="adsid", type="hidden")
		adsid1 = (adsid[0]["value"])
	except:
		sys.stdout.write("\r")
		sys.stdout.write("                                   ")
		sys.stdout.write("\r")
		sys.stdout.write("\033[1;31mSoory, There are no ads available\n")
		sys.stdout.flush()
		sleep(1)
		sys.exit()
		pass
	
	
	#print(adsid1)
	
	sys.stdout.write("\r")
	sys.stdout.write("                           ")
	sys.stdout.write("\r")
	sys.stdout.write(purple+"Getting Balanace")
	sys.stdout.flush()
	sleep(3)

	sys.stdout.write("\r")
	sys.stdout.write("                                ")
	sys.stdout.write("\r")
	sys.stdout.write(green+"Your Balance: "+bal+"\n")
	sys.stdout.flush()
	
	pattern = "var viewurl = '(.*?)';"
	match_results = re.search(pattern, sss, re.IGNORECASE)
	title = match_results.group()
	title = re.sub("<.*?>", "", title) #.replace("var viewurl = '", "").split
	stripped_of = re.sub("var viewurl = '", "", title) #.replace("'", "").replace(";", "")  # Remove HTML tags
	stripped_of_url = re.sub("';", "", stripped_of)
		
	pattern = "var viewtime = '(.*?)';"
	match_results = re.search(pattern, sss, re.IGNORECASE)
	title = match_results.group()
	title = re.sub("<.*?>", "", title)
	stripped_of_time = re.sub("var viewtime = '", "", title)
	stripped_of_time1 = re.sub("';", "", stripped_of_time)
	
	
	sys.stdout.write("\r")
	sys.stdout.write("                                ")
	sys.stdout.write("\r")
	sys.stdout.write(green+"visiting web ")
	sys.stdout.flush()
	sleep(2)
	
	
	
	
	
	time2 = (stripped_of_time1.strip())
	tunggu(int(time2))
		
	post_header = {
	'Host':'adltc.cc',
	'user-agent': obj['User-Agent'],
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'referer':'https://adltc.cc/surf',
	'cookie': obj['Cookies']
	}
	json="adsids="+adsid1
	resp = c.post("https://adltc.cc/earndata.php",  data=json, headers=post_header, timeout=15, allow_redirects=True)
	js = (resp.text)
	#print(bal)
	header = {
	'Host': 'adltc.cc',
	'user-agent': obj['User-Agent'],
	'cookie': obj['Cookies']
	}
	
	#print(bal)
	
		