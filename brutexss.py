from string import whitespace
import string
import httplib
import urllib
import socket
import urlparse
import os
import sys
import time
from colorama import init , Style, Back,Fore
import mechanize
import httplib
import introduce

init()


def wordlistimport(file,lst):
		try:
			with open(file,'r') as f: #Importing Payloads from specified wordlist.
				print(Style.DIM+Fore.WHITE+"[+] Loading Payloads from specified wordlist..."+Style.RESET_ALL)
				for line in f:
					final = str(line.replace("\n",""))
					lst.append(final)
		except IOError:
			print(Style.BRIGHT+Fore.RED+"[!] Wordlist not found!"+Style.RESET_ALL)



def GET():
    print "[!] URL Example: http://thegioiso.vn/search.php?kw=test"
    site = raw_input ("[?] Enter URL: ")
    #site = "http://192.168.141.131/bWAPP/xss_get.php?firstname=d&lastname=d&form=submit"
    #site = "http://thegioiso.vn/search.php?kw=test"
    if 'http://' in site:
        pass
    elif 'https://' in site:
        pass
    else:
        site = "http://"+site

    payloads = []
    newPlayloads = []
    wordlist = 'wordlist.txt'
    wordlistimport (wordlist, payloads)

    paravalue = []
    finalurl = urlparse.urlparse(site)
    parameters = urlparse.parse_qs (finalurl.query, keep_blank_values=True)

    for para in parameters:
        for i in parameters[para]:
            if i!='submit':
                paravalue.append(i)


    query = finalurl.query

    for payl in payloads:
        for para in paravalue:
            temp = query.replace(para,payl)
            urlForPayloads = finalurl.scheme+"://"+finalurl.hostname+finalurl.path+"?"+temp
            newPlayloads.append(urlForPayloads)
            print urlForPayloads

    countVul = 0;

    for inj,payl in zip(newPlayloads,payloads):

        page = urllib.urlopen(inj)
        if payl in page.read():
            countVul +=1


    if countVul!=0:
        print "[------>]"+str(countVul)+" Payloads XSS Vulnerability Found!"
    else:
        print "Not Payloads XSS Vul"





def brutexss():

    introduce.banner()

    methodselect = raw_input ("[?] Select method: [G]ET or [P]OST (G/P): ").lower ()

    if methodselect == 'g':
        GET ()
    elif methodselect == 'p':
        pass
    else:
        print("[!] Incorrect method selected.")



brutexss()

