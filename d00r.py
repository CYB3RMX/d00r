#!/usr/bin/env python3

# Configuring color variables
yellow='\u001b[1;93m'
cyan = '\u001b[1;96m'
red = '\u001b[1;91m'
green = '\u001b[1;92m'
white = '\u001b[1;37;40m'

thread_num = 1 # Number of threads
hits = []
import requests, os, sys, argparse, threading, queue
try:
    from tqdm import tqdm
except:
    print("Missing modules: tqdm")
    sys.exit(1)

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

# Parsing and handlig arguments
args = []
parser = argparse.ArgumentParser()
parser.add_argument("--url", required=False, help="Enter a target url.")
parser.add_argument("--wordlist", required=False, help="Select a wordlist.")
parser.add_argument("--status", required=False, nargs='+', help="Filter status codes.")
parser.add_argument("--install", required=False, help="Install d00r on your system.", action="store_true")
parser.add_argument("--thread", required=False, help="How many thread do you want ?")
args = parser.parse_args()
global q

if args.install:
    if os.getuid() != 0:
        print(f"{cyan}[{red}!{cyan}]{white} Use this argument with root privileges.")
    else:
        command = "cp d00r.py d00r; chmod +x d00r; sudo mv d00r /usr/bin/"
        os.system(command)
if args.thread is not None:
        thread_num = int(args.thread)

# Using the arguments
targeturl = str(args.url)
try:
    wlist = open(args.wordlist,'r').read().split('\n')
except:
    print(f"{cyan}[{red}!{cyan}]{white} Please use -h to see available arguments")
    sys.exit(1)

# Checking how many words in that list and putting in queue
count=0
q = queue.Queue()
for w in wlist:
    q.put(w)
    count+=1 

# Outputs
print(f"{cyan}[{red}*{cyan}]{white} Target URL: {targeturl}")
print(f"{cyan}[{red}*{cyan}]{white} Wordlist: {args.wordlist}")
print(f"{cyan}[{red}*{cyan}]{white} Status Codes: {args.status}")
print(f"\n{cyan}[{red}*{cyan}]{white} d00r IS CHECKING DIRECTORIES PLEASE WAIT [CTRL+C TO STOP]...")
print("\n") 

# Scanner (brute-force) function
def scanner():
    counter = 0
    try:
        while not q.empty():
            inject = q.get()
            kn0ck = '{}/{}'.format(targeturl,inject)
            r = requests.get(kn0ck)
            ret = f'{r.status_code}'           
            if ret in args.status:
                print(f"Status {green}{ret}{white} => {green}{kn0ck}{white}")
                hits.append((kn0ck,ret))

    except KeyboardInterrupt:
        print(f"\n{cyan}[{red}!{cyan}]{white} Program terminated by user.")

# Handling threads
ts = []
for i in range(0,thread_num):
    try:
        t = threading.Thread(target=scanner)
        ts.append(t)
        t.start()
    except Exception as e:
        print(e)
for t in ts:
    t.join()
