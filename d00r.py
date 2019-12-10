#!/usr/bin/env python

# Colors
yellow = '\033[93m'
cyan = '\033[96m'
red = '\033[91m'
magenta = '\033[95m'
default = '\033[0m'

# Importing modules and checking missing ones.
import requests,os,sys
try:
    from tqdm import tqdm
except ImportError:
    print("Module: tqdm not found please do >>> pip3 install tqdm <<<")
    sys.exit(1)

# Global variables
wlist = open('crawl.txt','r').read().split('\n')
check = ""
count = 0
for itera in wlist: # Checking how many words in that list
    count+=1
valid_directory = [] # Valid directory list
forb_directory = [] # Forbidden directory list

# Banner
screen='''
      _  ___   ___
     | |/ _ \ / _ \\
   __| | | | | | | |_ __
  / _` | | | | | | | '__|
 | (_| | |_| | |_| | |
  \__,_|\___/ \___/|_|

  >> Attention s0me0n3 kn0ck th3 d00r !!

             >[By CYB3RMX_]<
'''
os.system('clear')
print(yellow)
print(screen)

# Functions
class d00r:
    def Outputs():
        try:
            if valid_directory == []:
                print("{}[{}!{}]{} No any valid directories found.".format(cyan,red,cyan,default))
            else:
                print("\n{}[{}*{}]{} Valid Directoires (HTTP CODE: 200):".format(cyan,red,cyan,default))
                print("------------------------------------------------")
                for valid in valid_directory:
                    print("{}{}".format(cyan,valid))
                print("{}------------------------------------------------\n\n".format(default))
            if forb_directory == []:
                print("{}[{}!{}]{} No any forbidden directories found.".format(cyan,red,cyan,default))
            else:
                print("{}[{}*{}]{} Forbidden Directories (HTTP CODE: 403):".format(cyan,red,cyan,default))
                print("------------------------------------------------")
                for forbidden in forb_directory:
                    print("{}{}".format(magenta,forbidden))
                print("{}------------------------------------------------".format(default))
        except KeyboardInterrupt:
            if valid_directory == []:
                print("{}[{}!{}]{} No any valid directories found.".format(cyan,red,cyan,default))
            else:
                print("\n{}[{}*{}]{} Valid Directories (HTTP CODE: 200):".format(cyan,red,cyan,default))
                print("------------------------------------------------")
                for valid in valid_directory:
                    print("{}{}".format(cyan,t))
                print("{}------------------------------------------------\n\n".format(default))
            if forb_directory == []:
                print("{}[{}!{}]{} No any forbidden links found.".format(cyan,red,cyan,default))
            else:
                print("{}[{}*{}]{} Forbidden Directories (HTTP CODE: 403):".format(cyan,red,cyan,default))
                print("------------------------------------------------")
                for forbidden in forb_directory:
                    print("{}{}".format(magenta,f))
                print("{}------------------------------------------------".format(default))
    def BruteZone():
        try:
            print("\n{}[{}*{}]{} d00r IS CHECKING DIRECTORIES PLEASE WAIT [CTRL+C TO STOP]...".format(cyan,red,cyan,default))
            for i in tqdm(range(0,count), desc="Testing words"):
                inject = wlist[i]
                kn0ck = 'http{}://{}/{}'.format(check,targeturl.replace("http://","").replace("https://",""),inject)
                response = requests.get(kn0ck)
                ret = str(response.status_code)
                if ret == '200':
                    valid_directory.append(kn0ck)
                elif ret == '403':
                    forb_directory.append(kn0ck)
            d00r.Outputs()
        except:
            d00r.Outputs()
# Menu area
try:
    select = 0
    targeturl = str(input("{}[{}+{}]{} ENTER TARGET URL: ".format(cyan,red,cyan,default)))
    if "http" not in targeturl:
        print("{}[{}1{}]{} HTTP".format(cyan,red,cyan,default))
        print("{}[{}2{}]{} HTTPS".format(cyan,red,cyan,default))
        select = int(input("\n{}[{}+{}]{} CHOOSE: ".format(cyan,red,cyan,default)))
    print("https" in targeturl)
    if "https" in targeturl: 
        check = "s"
    if select == 2:
        check = "s"
    d00r.BruteZone()
except:
    print("{}[{}!{}]{} Program interrupted.".format(cyan,red,cyan,default))

