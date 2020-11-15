#Script By Sandaru Ashen https://t.me/Sl_Sanda_Ru
from os import system,name,path,mkdir,getcwd
from time import sleep
from random import choice
from sys import stdout
try:
	from clint.textui import progress
	from colorama import Fore,init
	from requests import get,patch
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print('\x1b[91m\x1b[1m[!] Required Dependencies Aren\'t Installed!')
	sleep(0.5)
	print('\x1b[92m\x1b[1m[*] Installing...')
	system('pip3 install -r requirements.txt')
	from colorama import Fore,init
	from requests import get
	from clint.textui import progress
	from bs4 import BeautifulSoup
if path.exists('Downloaded'):
	pass
else:
	mkdir('Downloaded')
init(autoreset=True)
run = 'python3 main.py' if name == 'posix' else 'python.exe main.py'
#Colors
blu=Fore.BLUE
cya=Fore.CYAN
gre=Fore.GREEN
yel=Fore.YELLOW
red=Fore.RED
mag=Fore.MAGENTA
liyel=Fore.LIGHTYELLOW_EX
lired=Fore.LIGHTRED_EX
limag=Fore.LIGHTMAGENTA_EX
liblu=Fore.LIGHTBLUE_EX
licya=Fore.LIGHTCYAN_EX
ligre=Fore.LIGHTGREEN_EX
rst=Fore.RESET
bold='\x1b[1m'
fore=list((blu,cya,gre,yel,red,mag,liyel,lired,limag,liblu,licya,ligre))
cle = 'clear' if name == 'posix' else 'cls'
#Downloader Copied From Stackoverflow
def dwnlder(url,out):
	r = get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'},stream=True)
	with open(out, 'wb') as f:
	    total_length = int(r.headers.get('content-length'))
	    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
	        if chunk:
	            f.write(chunk)
	            f.flush()
def spinner():
        l=['|','/','-','\\']
        for i in l+l+l:
                stdout.write('\r'+bold+liyel+'[*] Checking Your Internet Connection  '+choice(fore)+i)
                stdout.flush()
                sleep(0.2)
def dlo_li_find(soup):
	return soup.find('a',class_='btn',rel='nofollow',id='link').attrs['href']
logo=f'{choice(fore)}\x1b[1m       ________  ________.________.__     __  __.\n___  __\\_____  \\/  _____/|   ____/|  |   |  |/ _|\n\\  \\/  //  ____/   __  \\ |____  \\ |  |   |    <  \n >    </       \\  |__\\  \\/       \\|  |___|  |  \\ \n/__/\\_ \\_______ \\_____  /______  /|_____ \\__|__ \\\n      \\/       \\/     \\/       \\/       \\/     \\/\n{choice(fore)}\t     _________ .____    .___ \n\t     \\_   ___ \\|    |   |   |\n\t     /    \\  \\/|    |   |   |\n\t     \\     \\___|    |___|   |\n\t      \\______  /_______ \\___| v.1.1\n\t\t     \\/        \\/    \n\t\t{choice(fore)}[+] By Sandaru Ashen'
bar=f'{choice(fore)}\x1b[1m_________________________{choice(fore)}_________________________\x1b[0m'
system(cle)
print(bar+'\n')
print(logo)
print(bar+'\n')
print('\x1b[1m\t\t\x1b[92m1.Start x265LK-CLI\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
while True:
	try:
		cho=int(input(licya+bold+'Enter Your Choice: '))
		if cho > 0 and cho < 4:
			break
		else:
			print(lired+bold+'[!] Please Enter A Correct Choice!')
	except ValueError:
		print(lired+bold+'[!] Incorrect Choice')
if cho == 3:
	exit()
elif cho == 2:
	sleep(0.4)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'{bold}\t\t\t      About\n{choice(fore)}[+] This Script Is Only For Personal Use\n{choice(fore)}[+] If You Have Any Complains Or Future Requests Contact Me @ https://t.me/Sl_Sanda_Ru\n{choice(fore)}[+] This Script Was Created To Test My Skills After Doing An Udemy Course')
	input(f'{bold}{choice(fore)}\t[+] Press ENTER To Go Back To Main Menu')
	system(run)
else:
	sleep(0.4)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		spinner()
		patch('https://a9c3af23099293570b4ae5a5c60e0762.m.pipedream.net')
		print(gre+bold+'\n[+] Connection Successful')
	except Exception:
		sleep(0.4)
		print(lired+bold+'\n[!] You Aren\'t Connected To Internet!')
		sleep(0.3)
		print(lired+bold+'[!] Please Connect To Internet To Continue...')
		sleep(0.3)
		input(lired+bold+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	sleep(0.4)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	while True:
		param = {'s':input(bold+choice(fore)+'[+] Enter Title Of The Movie Or Tv Series: ')}
		if param['s']:
			break
		else:
			print(bold+lired+'[!] Wrong Input!\nTry Again')
	sea_res_soup=BeautifulSoup(get('https://www.x265lk.com/',params=param).text,'html.parser')
	if not sea_res_soup.find_all('div',class_='title'):
		print(bold+red+'No Results')
		exit()
	sea_res_title=[];sea_res_year=[];sea_res_rati=[];sea_res_type=[];sea_res_link=[]
	for i in sea_res_soup.find_all('article'):
		try:
			sea_res_title.append(i.find('div',class_='title').get_text())
			try:
				sea_res_year.append(i.find('span',class_='year').get_text())
			except AttributeError:
				sea_res_year.append('-')
			try:
				sea_res_rati.append(i.find('span',class_='rating').get_text())
			except AttributeError:
				sea_res_rati.append('-')
			if i.find('span',class_='movies'):
				sea_res_type.append('Movie')
			elif i.find('span',class_='tvshows'):
				sea_res_type.append('TV Series')	
			sea_res_link.append(i.find('a').attrs['href'])
		except:
			pass
	'''for i in sea_res_soup.find_all('div',class_='title'):
		sea_res_title.append(i.find('a').get_text())
	for i in sea_res_soup.find_all('span',class_='year'):
		sea_res_year.append(i.get_text())
	for i in sea_res_soup.find_all('span',class_='rating'):
		sea_res_rati.append(i.get_text())
	for i in sea_res_soup.find_all('article'):
		if i.find('span',class_='movies'):
			sea_res_type.append('Movie')
		elif i.find('span',class_='tvshows'):
			sea_res_type.append('TV Series')
	for i in sea_res_soup.find_all('article'):
		sea_res_link.append(i.find('a').attrs['href'])
	for i in sea_res_soup.find_all('article'):
		if i.attrs:
			pass
		else:
			sea_res_link.append(i.find('a').attrs['href'])'''
	tmp = param['s']
	print(f'{choice(fore)}{bold}  Search Results For \'{tmp}\':')
	for i in range(1,(len(sea_res_title)+1)):
		print('   '+bold+choice(fore)+str(i)+')'+sea_res_title[i-1]+' '+sea_res_year[i-1]+' '+sea_res_type[i-1]+' '+sea_res_rati[i-1])
	while True:
	  try:
	    sel_tit_no=int(input(f'{bold}{choice(fore)}[+] Enter The Number Of The Title You Want To Download: '))
	    if sel_tit_no > len(sea_res_title) or sel_tit_no < 1:
	      print(red+bold+'[!] Invalid Title Number')
	    else:
	      break
	  except ValueError:
	    print(red+bold+'[!] Invalid Title Number')
	sel_ite_soup=BeautifulSoup(get(sea_res_link[sel_tit_no-1]).text,'html.parser')
	item=dict()
	item['title']=sel_ite_soup.find('h1').get_text()
	try:
		item['rele_dat']=sel_ite_soup.find('span',class_='date',itemprop='dateCreated').get_text()
	except AttributeError:
		item['rele_dat']='-'
	item['desc']=sel_ite_soup.find('p').get_text()
	item['genre']=[]
	tmp=sel_ite_soup.find('div',class_='sgeneros')
	for i in tmp.find_all('a'):
		item['genre'].append(i.get_text())
	if sea_res_type[sel_tit_no-1]=='Movie':
		try:
			item['country']=sel_ite_soup.find('span',class_='country').get_text()
		except AttributeError:
			item['country']='-'
		try:
			item['dura']=sel_ite_soup.find('span',class_='runtime',itemprop='duration').get_text()[:-1]+'utes'
		except AttributeError:
			item['dura']='-'
		try:
			item['rati']=sel_ite_soup.find('b',id='repimdb').get_text()
		except AttributeError:
			item['rati']=sel_ite_soup.find_all('span',class_='valor')[-1].get_text()
		item['fqual']=[];item['dlolin']=[];item['fsize']=[]
		for i in sel_ite_soup.find_all('strong',class_='quality'):
			item['fqual'].append(i.get_text())
		for i in sel_ite_soup.find_all('a',target='_blank'):
			item['dlolin'].append(i.attrs['href'])
		for i in sel_ite_soup.find_all('td'):
			if i.get_text()[-2:] == 'MB':
				item['fsize'].append(i.get_text())
			elif i.get_text()[-2:] == 'GB':
				item['fsize'].append(i.get_text())
			else:
				pass
		system('clear')
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
		print(f'{bold}{choice(fore)}Title: {choice(fore)}{item["title"]}\n{choice(fore)}Release Date: {choice(fore)}{item["rele_dat"]}\n{choice(fore)}Country: {choice(fore)}{item["country"]}\n{choice(fore)}Duration: {choice(fore)}{item["dura"]}\n{choice(fore)}Rating: {choice(fore)}{item["rati"]}\n{choice(fore)}Genres: {choice(fore)}{",".join(item["genre"])}\n{choice(fore)}Description: {choice(fore)}{item["desc"]}')
		print(bold+choice(fore)+'Download Files:')
		for i in range(1,len(item['fqual'])+1):
			print(f'  {bold}{choice(fore)}{i}) {item["fqual"][i-1]} {item["fsize"][i-1]}')
		while True:
			try:
				sel_dlo_no=int(input(f'{bold}{choice(fore)}[+] Enter File Number You Want To Download: '))
				if sel_dlo_no > len(item['fqual']) or sel_dlo_no < 1:
					print(bold+lired+'[!] Please Enter A Valid Number')
				else:
					break
			except ValueError:
				print(bold+lired+'[!] Enter Number Not Character')
		dlo_pag_soup=BeautifulSoup(get(item['dlolin'][sel_dlo_no-1]).text,'html.parser')
		sel_ite_doli=dlo_li_find(dlo_pag_soup)
		while True:
			try:
				cho=int(input(f'{bold}{choice(fore)}[+] Input 1 To Download File Directly Or 2 To Get Download Link: '))
				if cho < 1 or cho >2:
					print(f'{bold}{lired}[!] Wrong Input')
				else:
					break
			except ValueError:
				print(f'{bold}{lired}[!] Invalid Input')
		if cho == 1:
			system(cle)
			print(bar+'\n')
			print(logo)
			print(bar+'\n')
			url=sel_ite_doli
			fldr_nam=url[url.rfind("/")+1:url.rfind(".")]
			try:
				mkdir(f'Downloaded/{fldr_nam}')
			except FileExistsError:
				print(f'{bold}{red}[!] File Already Exists')
				exit()
			print(bold+yel+'Downloading '+f'{fldr_nam}{url[url.rfind("."):]}')
			dwnlder(url, f'Downloaded/{fldr_nam}/{fldr_nam}{url[url.rfind("."):]}')
			print(f'{bold}{ligre}Downloaded {fldr_nam}{url[url.rfind("."):]} To {getcwd()}/{fldr_nam}{url[url.rfind("."):]}')
		else:
			print(sel_ite_dlpag+f'{bold}{choice(fore)}\nCopy & Paste The URL In Your Favourite Download Manager To Download')

	else:
		tmp = sel_ite_soup.find_all('span')
		item['maker']=[]
		for i in tmp:
			for ii in i.find_all('a',rel='tag'):
				item['maker'].append(ii.get_text())
		tmp = []
		for i in sel_ite_soup.find_all('span',class_='se-t'):
			tmp.append(i.get_text())
		item['no_seas']=int(max(tmp))
		item['epi']=[]
		for i in sel_ite_soup.find_all('div',class_='numerando'):
			item['epi'].append(i.get_text())
		for i in enumerate(sel_ite_soup.find_all('div',class_='episodiotitle')):
			item['epi'][i[0]] += ' ' + i[1].get_text()
		tmp = item['epi']
		del item['epi']
		for i in range(1,item['no_seas']+1):
			exec(f'item[\'ses_{i}\'] = []')
		while True:
			ii = 1
			for i in tmp:
				if str(ii) == i[0]:
					item[f'ses_{ii}'].append(i)
				else:
					ii += 1
					item[f'ses_{ii}'].append(i)
			break
		system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
		print(f'{bold}{choice(fore)}[!] {sea_res_title[sel_tit_no-1]} Have {item["no_seas"]} Seasons')
		sleep(0.8)
		while True:
			try:
				sel_ses_no=int(input(f'{bold}{choice(fore)} [?] From Which Season You Wanna Download?: '))
				if sel_ses_no > item['no_seas'] or sel_ses_no < 1:
					print(bold+red+'[!] Invalid Number Of Season')
				else:
					break
			except ValueError:
				print(red+bold+'[!] Please Enter The Number Of The Season')
		for i in enumerate(item[f'ses_{sel_ses_no}']):
			print('    '+bold+choice(fore)+str(i[0]+1)+') '+i[1])
		while True:
			try:
				sel_ep_no=int(input(f'{bold}{choice(fore)} [?] Which Episode You Want To Download?: '))
				if sel_ep_no > len(item[f'ses_{sel_ses_no}']) or sel_ep_no < 1:
					print(bold+lired+'[!] Invalid Number')
				else:
					break
			except ValueError:
				print(red+bold+'[!] Please Enter The Number Of The Episode')
		tmp_ses_epi = item[f'ses_{sel_ses_no}'][sel_ep_no-1].split()[:3:2]
		tmp_name = sea_res_link[sel_tit_no-1].split('/')[-2]
		sel_ep_soup=BeautifulSoup(get(f'https://www.x265lk.com/episodes/{tmp_name}-{tmp_ses_epi[0]}x{tmp_ses_epi[1]}/').text,'html.parser')
		del tmp_name;del tmp_ses_epi
		sel_ep_dlolin=[];sel_ep_qual=[];sel_ep_fsiz=[]
		try:
			sel_ep_desc=sel_ep_soup.find('p').get_text()
		except AttributeError:
			sel_ep_desc='-'
		sel_ep_name=sel_ep_soup.find('h3',class_='epih3').get_text()
		sel_ep_date=sel_ep_soup.find('span',class_='date').get_text()
		for i in sel_ep_soup.find_all('a',target='_blank'):
				sel_ep_dlolin.append(i.attrs['href'])
		for i in sel_ep_soup.find_all('strong',class_='quality'):
				sel_ep_qual.append(i.get_text())
		for i in sel_ep_soup.find_all('td'):
				if i.get_text()[-2:] == 'MB' or i.get_text()[-2:] == 'GB':
					sel_ep_fsiz.append(i.get_text())
		system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
		print(f'{bold}{choice(fore)}Tv Series Name: {choice(fore)}{sea_res_title[sel_tit_no-1]}\n{choice(fore)}Episode Name: {choice(fore)}{sel_ep_name}\n{choice(fore)}Date: {choice(fore)}{sel_ep_date}\n{choice(fore)}Description: {choice(fore)}{sel_ep_desc}\n{choice(fore)}Download Files: ')
		for i in range(1,len(sel_ep_qual)+1):
			print(f'  {bold}{choice(fore)}{i}) {sel_ep_qual[i-1]} {sel_ep_fsiz[i-1]}')
		while True:
			try:
				cho=int(input(f'{bold}{choice(fore)}[?] Which File Do You Want To Download?: '))
				if cho < 1 or cho > len(sel_ep_qual):
					print(bold+lired+'[!] Invalid Number')
				else:
					break
			except ValueError:
				print(bold+red+'[!] Please Enter The File Number')
		sel_ep_dlopag=BeautifulSoup(get(sel_ep_dlolin[cho-1]).text,'html.parser')
		while True:
			try:
				cho=int(input(f'{bold}{choice(fore)}[+] Input 1 To Download File Directly Or 2 To Get Download Link: '))
				if cho < 1 or cho >2:
					print(f'{bold}{lired}[!] Wrong Input')
				else:
					break
			except ValueError:
				print(f'{bold}{lired}[!] Invalid Input')
		if cho == 1:
			system(cle)
			print(bar+'\n')
			print(logo)
			print(bar+'\n')
			url=dlo_li_find(sel_ep_dlopag)
			fldr_nam=url[url.rfind("/")+1:url.rfind(".")]
			try:
				mkdir(f'Downloaded/{fldr_nam}')
			except FileExistsError:
				print(f'{bold}{red}[!] File Already Exists')
				exit()
			print(bold+yel+'Downloading '+f'{fldr_nam}{url[url.rfind("."):]}')
			dwnlder(url, f'Downloaded/{fldr_nam}/{fldr_nam}{url[url.rfind("."):]}')
			print(f'{bold}{ligre}Downloaded {fldr_nam}{url[url.rfind("."):]} To {getcwd()}/{fldr_nam}{url[url.rfind("."):]}')
		else:
			print(dlo_li_find(sel_ep_dlopag)+f'{bold}{choice(fore)}\nCopy & Paste The URL In Your Favourite Download Manager To Download')
