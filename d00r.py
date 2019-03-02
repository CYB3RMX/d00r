#!/usr/bin/env python
green='\u001b[92m'
red='\u001b[91m'
white='\u001b[0m'
yellow='\u001b[93m'
import requests,os
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
try:
     print(yellow)
     print(screen)
     print(white)
     targeturl=str(input("ENTER TARGET URL: "))
     print("[+] CRAWL STARTS...")
     wlist=open('crawl.txt','r')
     valid=[]
     for i in wlist:
        print(white)
        print("-------------------------------------------------")
        print("[+] TESTING: http://{}/{}".format(targeturl,i))
        kn0ck='http://{}/{}'.format(targeturl,i)
        r=requests.get(kn0ck)
        ret=str(r.status_code)
        if ret == '404':
          print("\u001b[91m[*] NOT FOUND: {}".format(kn0ck))
          print("\u001b[0m-------------------------------------------------")
        else:
          print("\u001b[92m[*] FOUND: {}".format(kn0ck))
          print("\u001b[0m-------------------------------------------------")
          valid.append(kn0ck)
except KeyboardInterrupt:
     print("[*] VALID LOGIN LINKS:")
     for t in valid:
        print("\u001b[96m"+t)
