#!/usr/bin/env python
yellow='\u001b[93m'

import requests,os,sys
from tqdm import tqdm

screen='''
      _  ___   ___
     | |/ _ \ / _ \\
   __| | | | | | | |_ __
  / _` | | | | | | | '__|
 | (_| | |_| | |_| | |
  \__,_|\___/ \___/|_|    v1.0

  >> Attention s0me0n3 kn0ck th3 d00r !!

             >[By CYB3RMX_]<
'''
os.system('clear')
print(yellow)
print(screen)

# Menu area
print("\033[96m[\033[91m1\033[96m]\033[0m HTTP")
print("\033[96m[\033[91m2\033[96m]\033[0m HTTPS")
try:
    select = int(input("\n\033[96m[\033[91m+\033[96m]\033[0m CHOOSE: "))
except:
    print("\033[96m[\033[91m!\033[96m]\033[0m Program terminated.")
    sys.exit(1)
# Scanner (brute-force) function
def Scanner():
    check = ""
    count = 0
    if select == 2:
        check = "s" # That is for scanning https
    try:
        targeturl = str(input("\033[96m[\033[91m+\033[96m]\033[0m ENTER TARGET URL: "))
        wlist = open('crawl.txt','r').read().split('\n')
        for itera in wlist: # Checking how many words in that list
            count+=1

        valid = [] # Valid links
        forb = [] # Forbidden links

        print("\n\033[96m[\033[91m*\033[96m]\033[0m d00r IS CHECKING DIRECTORIES PLEASE WAIT [CTRL+C TO STOP]...")
        for i in tqdm(range(0,count), desc="Testing words"):
            inject = wlist[i]
            kn0ck = 'http{}://{}/{}'.format(check,targeturl,inject)
            r = requests.get(kn0ck)
            ret = str(r.status_code)
            if ret == '404':
                pass
            elif ret == '403':
                forb.append(kn0ck)
            elif ret == '200':
                valid.append(kn0ck)
        if valid == []:
            pass
        else:
            print("\n\033[96m[\033[91m*\033[96m]\033[0m VALID LOGIN LINKS (HTTP CODE: 200):")
            print("------------------------------------------------")
            for t in valid:
                print("\u001b[96m"+t)
            print("\u001b[0m------------------------------------------------\n\n")
        if forb == []:
            pass
        else:
            print("\033[96m[\033[91m*\033[96m]\033[0m FORBIDDEN LINKS (HTTP CODE: 403):")
            print("------------------------------------------------")
            for f in forb:
                print("\u001b[95m"+f)
            print("\u001b[0m------------------------------------------------")
    except KeyboardInterrupt:
        if valid == []:
            pass
        else:
            print("\n\033[96m[\033[91m*\033[96m]\033[0m VALID LOGIN LINKS:")
            print("------------------------------------------------")
            for t in valid:
                print("\u001b[96m"+t)
            print("\u001b[0m------------------------------------------------\n\n")
        if forb == []:
            pass
        else:
            print("\033[96m[\033[91m*\033[96m]\033[0m FORBIDDEN LINKS:")
            print("------------------------------------------------")
            for f in forb:
                print("\u001b[95m"+f)
            print("\u001b[0m------------------------------------------------")
if __name__ == '__main__':
    Scanner()
