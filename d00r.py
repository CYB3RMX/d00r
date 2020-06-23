#!/usr/bin/env python3

# Configuring color variables
yellow='\u001b[1;93m'
cyan = '\u001b[1;96m'
red = '\u001b[1;91m'
white = '\u001b[1;37;40m'

import requests,os,sys,argparse
try:
    from tqdm import tqdm
except:
    print("Missing modules: tqdm")
    sys.exit(1)

# Banner
screen='''
      _  ___   ___
     | |/ _ \ / _ \\
   __| | | | | | | |_ __
  / _` | | | | | | | '__|
 | (_| | |_| | |_| | |
  \__,_|\___/ \___/|_|    v1.3

  >> URL Brute-Force Tool

             >[By CYB3RMX_]<
'''
os.system('clear')
print(yellow)
print(screen)

# Link variables
valid = [] # Valid links HTTP CODE: 200
forb = [] # Forbidden links HTTP CODE: 403
moved = [] # Moved perma links HTTP CODE: 301

# Printing function
def PrintSummary():
    # Valid links
    if valid == []:
        pass
    else:
        print("\n{}[{}+{}]{} VALID LOGIN LINKS (HTTP CODE: 200):".format(cyan,red,cyan,white))
        print("------------------------------------------------")
        for t in valid:
            print("\u001b[1;96m"+t)
        print("{}------------------------------------------------\n\n".format(white))
    
    # Moved links
    if moved == []:
        pass
    else:
        print("{}[{}+{}]{} MOVED LINKS (HTTP CODE: 301):".format(cyan,red,cyan,white))
        print("------------------------------------------------")
        for m in moved:
            print("\u001b[1;95m"+m)
        print("{}------------------------------------------------".format(white))
    
    # Forbidden links
    if forb == []:
        pass
    else:
        print("{}[{}+{}]{} FORBIDDEN LINKS (HTTP CODE: 403):".format(cyan,red,cyan,white))
        print("------------------------------------------------")
        for f in forb:
            print("\u001b[1;95m"+f)
        print("{}------------------------------------------------".format(white))
    
        
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
            elif ret == '301':
                moved.append(kn0ck)
        
        # Print links
        PrintSummary()
    except KeyboardInterrupt:
        
        # If any exception occures print and exit
        PrintSummary()

# Execution
Scanner()