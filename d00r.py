#!/usr/bin/env python3

# Configuring color variables
yellow='\u001b[93m'
cyan = '\u001b[96m'
red = '\u001b[91m'
white = '\u001b[0m'

import requests,os,sys,argparse
from tqdm import tqdm

# Banner
screen='''
      _  ___   ___
     | |/ _ \ / _ \\
   __| | | | | | | |_ __
  / _` | | | | | | | '__|
 | (_| | |_| | |_| | |
  \__,_|\___/ \___/|_|    v1.2

  >> Attention s0me0n3 kn0ck th3 d00r !!

             >[By CYB3RMX_]<
'''
os.system('clear')
print(yellow)
print(screen)

# Scanner (brute-force) function
def Scanner():
    # Creating arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=False, help="Enter a target url.")
    parser.add_argument("-w", "--wordlist", required=False, help="Select a wordlist.")
    parser.add_argument("--install", required=False, help="Install d00r on your system.", action="store_true")
    args = parser.parse_args()
    if args.install:
        if os.getuid() != 0:
            print("{}[{}!{}]{} Use this argument with root privileges.".format(cyan,red,cyan,white))
        else:
            command = "cp d00r.py d00r; chmod +x d00r; sudo mv d00r /usr/bin/"
            os.system(command)
    try:
        # Using the arguments
        targeturl = str(args.url)
        try:
           wlist = open(args.wordlist,'r').read().split('\n')
        except:
           print("{}[{}!{}]{} Please use -h to see available arguments".format(cyan,red,cyan,white))
           sys.exit(1)
        count=0
        for itera in wlist: # Checking how many words in that list
            count+=1

        valid = [] # Valid links HTTP CODE: 200
        forb = [] # Forbidden links HTTP CODE: 403

        # Brute-force zone
        print("{}[{}*{}]{} Target URL: {}".format(cyan,red,cyan,white,targeturl))
        print("{}[{}*{}]{} Wordlist: {}".format(cyan,red,cyan,white,args.wordlist))
        print("\n{}[{}*{}]{} d00r IS CHECKING DIRECTORIES PLEASE WAIT [CTRL+C TO STOP]...".format(cyan,red,cyan,white))
        for i in tqdm(range(0,count), desc="Testing words"):
            inject = wlist[i]
            kn0ck = '{}/{}'.format(targeturl,inject)
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
            print("\n{}[{}+{}]{} VALID LOGIN LINKS (HTTP CODE: 200):".format(cyan,red,cyan,white))
            print("------------------------------------------------")
            for t in valid:
                print("\u001b[96m"+t)
            print("{}------------------------------------------------\n\n".format(white))
        if forb == []:
            pass
        else:
            print("{}[{}+{}]{} FORBIDDEN LINKS (HTTP CODE: 403):".format(cyan,red,cyan,white))
            print("------------------------------------------------")
            for f in forb:
                print("\u001b[95m"+f)
            print("{}------------------------------------------------".format(white))
    except KeyboardInterrupt:
        if valid == []:
            pass
        else:
            print("\n{}[{}+{}]{} VALID LOGIN LINKS:".format(cyan,red,cyan,white))
            print("------------------------------------------------")
            for t in valid:
                print("\u001b[96m"+t)
            print("{}------------------------------------------------\n\n".format(white))
        if forb == []:
            pass
        else:
            print("{}[{}+{}]{} FORBIDDEN LINKS:".format(cyan,red,cyan,white))
            print("------------------------------------------------")
            for f in forb:
                print("\u001b[95m"+f)
            print("{}------------------------------------------------".format(white))
if __name__ == '__main__':
    Scanner()
