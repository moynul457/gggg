import importlib
# -*- coding: utf-8 -*-

try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bababindsix')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


logo = "\n\x1b[1;94m ______   _______ _________ _______  _       \n\x1b[1;94m(  ___ \\\  \n\x1b[1;94m|  (  8b        d8                                                                                                
 Y8,    ,8P                                                                                                 
  Y8,  ,8P                                                                                                  
   "8aa8"  ,adPPYba,   88       88  8b,dPPYba,     8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  
    `88'  a8"     "8a  88       88  88P'   "Y8     88P'   `"8a  ""     `Y8  88P'   "88"    "8a  a8P_____88  
     88   8b       d8  88       88  88             88       88  ,adPPPPP88  88      88      88  8PP"""""""  
     88   "8a,   ,a8"  "8a,   ,a88  88             88       88  88,    ,88  88      88      88  "8b,   ,aa  
     88    `"YbbdP"'    `"YbbdP'Y8  88             88       88  `"8bbdP"Y8  88      88      88   `"Ybbd8"' ) || (  \x1b[1;92mB\x1b[1;94m\n\x1b[1;94m| (_ || |  \x1b[1;93mA\x1b[1;94m\n\x1b[1;94m|  __ (  | |   | |   | |   | |   | || |  \x1b[1;96mB\x1b[1;94m\n\x1b[1;94m| (  \\ \\ | |   | |   | |   | |   | || |  \x1b[1;91mA\x1b[1;94m\n\x1b[1;94m| )___) )| (___) |   | |   | (___) || (____/\n\x1b[1;94m|/ \\___/ (_______)   )_(   (_______)(_______/\n\x1b[3;90m \n      IT'S NOT JUST A NAME, IT'S A BRAND\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mAUTHOR     : MEHEDI HASAN ARIYAN\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mFACEBOOK   : FACEBOOK.COM/THEMEHTAN\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mGITHUB     : GITHUB.COM/BOTOLMEHEDI\n\x1b[1;94m\xe"
cusr = 'THCB'

def u():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLOGIN APPROVAL'
    print '\x1b[1;97m--------------'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mPASSWORD : \x1b[1;96m')
    if usr == cusr:
        tik()
        zz()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97mLOGIN APPROVAL'
        print '\x1b[1;97m-------------'
        print '\x1b[1;97m '
        print '          \x1b[1;92mPASSWORD : \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://www.t.me/MasterTrick3')
        u()



def zz():
    os.system('clear')
    print logo
    print
    print
    print '\n\n \x1b[1;92mPASSWORD APPROVED BY BOTOL BABA.\x1b[0m'
    print
    jalan('\x1b[1;93mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING...')
    time.sleep(1)
    os.system('python2 .README.md')


if __name__ == '__main__':
    u()