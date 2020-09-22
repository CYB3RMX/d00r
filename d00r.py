#!/usr/bin/env python3

# Configuring color variables
yellow='\u001b[1;93m'
cyan = '\u001b[1;96m'
red = '\u001b[1;91m'
green = '\u001b[1;92m'
white = '\u001b[1;37;40m'

import requests,os,sys,argparse
try:
    from tqdm import tqdm
except:
    print("Missing modules: tqdm")
    sys.exit(1)

try:
    from prettytable import PrettyTable
except:
    print("Missing modules: prettytable")
    sys.exit(1)

# Banner
screen='''
      _  ___   ___
     | |/ _ \ / _ \\
   __| | | | | | | |_ __
  / _` | | | | | | | '__|
 | (_| | |_| | |_| | |
  \__,_|\___/ \___/|_|    v1.3.1

  >> URL Brute-Force Tool

             >[By CYB3RMX_]<
'''
print(f"{yellow}{screen}{white}")

# Creating parsing and handlig arguments
args = []
parser = argparse.ArgumentParser()
parser.add_argument("--url", required=False, help="Enter a target url.")
parser.add_argument("--wordlist", required=False, help="Select a wordlist.")
parser.add_argument("--status", required=False, nargs='+', help="Filter status codes.")
parser.add_argument("--install", required=False, help="Install d00r on your system.", action="store_true")
args = parser.parse_args()

# Valid links
urlAndCode = PrettyTable()
urlAndCode.field_names = [f"{green}URL{white}", f"{green}Status Code{white}"]

# Scanner (brute-force) function
def Scanner():
    if args.install:
        if os.getuid() != 0:
            print(f"{cyan}[{red}!{cyan}]{white} Use this argument with root privileges.")
        else:
            command = "cp d00r.py d00r; chmod +x d00r; sudo mv d00r /usr/bin/"
            os.system(command)
    try:
        # Using the arguments
        targeturl = str(args.url)
        try:
           wlist = open(args.wordlist,'r').read().split('\n')
        except:
           print(f"{cyan}[{red}!{cyan}]{white} Please use -h to see available arguments")
           sys.exit(1)
        
        # Checking how many words in that list
        count=0
        for _ in wlist:
            count+=1

        # Brute-force zone
        print(f"{cyan}[{red}*{cyan}]{white} Target URL: {targeturl}")
        print(f"{cyan}[{red}*{cyan}]{white} Wordlist: {args.wordlist}")
        print(f"{cyan}[{red}*{cyan}]{white} Status Codes: {args.status}")
        print(f"\n{cyan}[{red}*{cyan}]{white} d00r IS CHECKING DIRECTORIES PLEASE WAIT [CTRL+C TO STOP]...")
        for i in tqdm(range(0,count), desc="Testing URL's"):
            inject = wlist[i]
            kn0ck = '{}/{}'.format(targeturl,inject)
            r = requests.get(kn0ck)
            ret = f'{r.status_code}'
            if ret in args.status:
                urlAndCode.add_row([kn0ck, ret])
        
        # Printing zone
        if urlAndCode != "":
            print(urlAndCode)
    except KeyboardInterrupt:
        print(f"\n{cyan}[{red}!{cyan}]{white} Program terminated by user.")
        if urlAndCode != "":
            print(urlAndCode)

# Execution
Scanner()