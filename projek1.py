import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich.text import Text as tekz
#----------------------------------#
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#----------------------------------------------------#
def clear():
    os.system('clear')
#----------------------------------#
def boki(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.005)
#----------------------------------#
def wijaya(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
#---------------------------------------------------#
def banner():
  clear()
  cetak(nel("""\t [blue] _________               __               ______ 
\t|  _   _  |             [  |             |_   _ \           
\t[red]|_/ | | \_|.--.    .--.  | |  .--.  ______ | |_) |   .--.   _   __ 
 \t    | |  / .'`\ \/ .'`\ \| | ( (`\]|______||  __'. / .'`\ \[ \  [  ]
 \t[blue]   _| |_ | \__. || \__. || |  `'.'.       _| |__) || \__.  |  > ' < 
 \t  [white]|_____| '.__.'  '.__.'[___][\__) )     |_______/  '.__.' [__]`\_][white]

 \t  ([blue]-[white]) Tools Install Use In Python3.x
 \t  ([blue]-[white]) Suport [green]Linux[white],[green]Termux[white],[green]ComandPromp[white],[green]WindowsPowerShel[white]\n"""))
  ll=' |[green]+[white]| Author    :  Boki\n |[green]+[white]| Country   :  Indonesia\n |[green]+[white]| Instagram :  kikiwijya\n |[green]+[white]| Github    :  github.com/kiki-boki '
  nnk=nel(ll,style="")
  cetak(nel(nnk, title=' INFORMATION '))

def kiki():
  banner()
  mmk='([green]01[white]) Install Wifite ([green]UseWifiAdapter[white])\n([green]02[white]) Install Metasploit-Framework ([green]create payload[white])\n([green]03[white]) Install Sqlmap ([green]Get Databese WebVuln[white])\n([green]04[white]) Install Nmap ([green]Get Databese Web WorldPress[white])\n([green]05[white]) Install SETOOLKIT ([green]Phising Account[white])\n([green]06[white]) Install SEEKER ([green]Traper Locations Use [red]Ngrok[white])\n([green]07[white]) Install CamPhish ([green]Camera Phising Use [red]Ngrok[white])\n([yellow]00[white]) Massage Author '
  kntl=nel(mmk,style="")
  cetak(nel(kntl, title=' MENU '))
  jlt = input('    Chosee  :  ')
  if jlt in ['01','1']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd ..')
    os.system("git clone https://github.com/derv82/wifite2")
    clear()
    os.system('cd wifite2')
    clear()
    os.system('python2 Wifite.py')
  elif jlt in ['02','2']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('apt install wget')
    clear()
    os.system('apt isntall openssl')
    clear()
    os.system('cd')
    os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
    clear()
    os.system('chmod +x metasploit.sh')
    clear()
    os.system('./metasploit.sh')
  elif jlt in ['03','3']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    clear()
    os.system('cd sqlmap')
    clear()
    os.system('python sqlmap.py')
  elif jlt in ['04','4']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd')
    os.system('git clone https://github.com/nmap/nmap')
    clear()
    os.system('cd nmap')
    os.system('./configure')
    clear()
    os.system('make')
    os.system('make install')
    clear()
    os.system('nmap')
  elif jlt in ['05','5']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd')
    os.system('git clone https://github.com/trustedsec/social-engineer-toolkit')
    clear()
    os.system('cd social-engineer-toolkit')
    os.system('pip3 install -r requirements.txt')
    clear()
    os.system('python3 setup.py')
  elif jlt in ['06','6']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd')
    os.system('git clone https://github.com/thewhiteh4t/seeker')
    clear()
    os.system('cd seeker')
    os.system('bash install.sh')
    clear()
    os.system('python seeker.py')
  elif jlt in ['07','7']:
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    wijaya('Installing....')
    clear()
    os.system('cd')
    os.system('git clone https://github.com/techchipnet/CamPhish')
    clear()
    os.system('cd CamPhish')
    os.system('bash camphish.sh')
  elif jlt in ['00','0']:
    boki(f'Anda Akan Di Arah Kan Ke {h}WhatsApp{x}')
    time.sleep(2)
    os.system('xdg-open https://wa.me/6283192495253?text=Assalamualaikum+Bang+Kiki')
    kiki()
  elif jlt in ['']:
    boki('Input Not Found')
    time.sleep(2)
    kiki()
if __name__=='__main__':
  kiki()