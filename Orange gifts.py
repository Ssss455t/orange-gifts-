import requests,json
from bs4 import BeautifulSoup as BS
from time import sleep
import sys,os, time, json
print ('\033[1;92mclick on this link to get password👇')
print ()
link="\033[1;93mhttps://bestcash2020.com/zVI749xS"
print (link)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
if password !="Abdullah4550":
	print ('\033[1;91merror password !')
	print ('')
	exit()
else:
	logo='''\033[;091m

░█████╗░██████╗░░█████╗░███╗░░██╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝
██║░░██║██████╔╝███████║██╔██╗██║██║░░██╗░█████╗░░
██║░░██║██╔══██╗██╔══██║██║╚████║██║░░╚██╗██╔══╝░░
╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝

░██████╗░██╗███████╗████████╗░██████╗
██╔════╝░██║██╔════╝╚══██╔══╝██╔════╝
██║░░██╗░██║█████╗░░░░░██║░░░╚█████╗░
██║░░╚██╗██║██╔══╝░░░░░██║░░░░╚═══██╗
╚██████╔╝██║██║░░░░░░░░██║░░░██████╔╝
░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░

██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░

░█████╗░██████╗░██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██║░░░░░
███████║██████╦╝██║░░██║██║░░░██║██║░░░░░██║░░░░░
██╔══██║██╔══██╗██║░░██║██║░░░██║██║░░░░░██║░░░░░
██║░░██║██████╦╝██████╔╝╚██████╔╝███████╗███████╗
╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝

██╗░░░██╗██████╗░
██║░░░██║╚════██╗
╚██╗░██╔╝░█████╔╝
░╚████╔╝░░╚═══██╗
░░╚██╔╝░░██████╔╝
░░░╚═╝░░░╚═════╝░'''


	for I in logo +'\n':
		sys.stdout.write (I)
		sys.stdout.flush ()
		time.sleep (00.0010)
	print ()
	
	
	i='''\033[1;092mTelegram channel :
		
http://t.me/Techno0099            
	
	
Youttube channel  :  
	
https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg 
	 
	
Facebook  :  
	
https://www.facebook.com/AbdullahSalah0099/ 
	 
 '''
	
	for I in i +'\n':
		sys.stdout.write (I)
		sys.stdout.flush ()
		time.sleep (00.0030)
	print ('\033[1;93m*'*60)
	sleep (0.1)
	print ()
	
num=input ('\033[1;92m》Enter Number : \033[1;96m')
print ()
pas=input ('\033[1;92m》Enter password : \033[1;96m')
print ()
ctv=input ('\033[1;92m》Enter ctv :\033[1;96m ')
print ()
htv=input ('\033[1;92m》Enter htv : \033[1;96m')
print ()


url2="https://backend.orange.eg/api/WheelOfFortune/CheckEligibility"

headers2={
"_ctv":ctv,
"_htv":htv,

"isEasyLogin": "false",

"Content-Type": "application/json; charset=UTF-8",

"Content-Length": "190",

"Host": "backend.orange.eg",

"Connection": "Keep-Alive",

"Accept-Encoding": "gzip",

"User-Agent": "okhttp/3.12.0"
}

data2={"ServiceClassID":"1045","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"Dial":f"{num}","IsEasyLogin":False,"Lang":"ar","Password":f"{pas}"}
r2=requests.post (url2,headers=headers2,json=data2).json()
c=(r2["OfferId"])
#print (c)
#if c==:
#    print ('None')
if (r2["ErrorCode"]==9):
    print ('\033[1;91mError Number Or Password')
    exit()
elif (r2["ErrorCode"]==16):
    print ('\033[1;91mError ctv Or htv')
    exit()
elif (r2["OfferId"])=="" and (r2["ErrorCode"])==218:
    print ('\033[1;91mAttempts are Over , Try Tomorrow')
    exit()
elif (r2["ErrorCode"])==219:
    print ('\033[1;96mYou Took them before, Try After Some Days')
elif (r2["OfferId"])=="6":
	print ("Try your luck again")
elif (r2["OfferId"]=="9"):
	print ('Congratulations You Have 1000 Mg')
elif (r2["OfferId"])=="8":
    print ('Congratulations You Have 500 Mg')
elif (r2["OfferId"])=="10" or "3" or "2":
    print ('\033[1;96mCongratulation, You have 100 mg') 


print ('='*60)
sleep (2)



######################################


ctv1=input ('\033[1;92m》Enter a new ctv :\033[1;96m ')
print ()
htv1=input ('\033[1;92m》Enter a new htv : \033[1;96m')
print ()


url3="https://backend.orange.eg/api/WheelOfFortune/Offerfulfillment"

data3={"OfferID":f"{c}","ServiceClassID":"1044","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"Dial":f"{num}","IsEasyLogin":"false","Lang":"ar","Password":f"{pas}"}


headers3={
"_ctv": ctv1,

"_htv": htv1,

"isEasyLogin": "false",

"Content-Type": "application/json; charset=UTF-8",

"Content-Length": "190",

"Host": "backend.orange.eg",

"Connection": "Keep-Alive",

"Accept-Encoding": "gzip",

"User-Agent": "okhttp/3.12.0"
}

if True :
    r=requests.post(url3,headers=headers3,json=data3)
    print (r.text)
    print ()
    
    if (r.json()["ErrorCode"])==0:
        print ('\033[1;96mDone Add Megabytes')
    elif(r.json()["ErrorCode"])==13:
        print ('\033[1;91mctv & htv unexpired')
        print ('be fast')
        exit()
    elif (r.json()["ErrorCode"])==16:
        print ('\033[1;91mError ctv or htv')
        exit()
    elif (r.json()["ErrorCode"])==9:
        print ('\033[1;91mError Number Or Password')
        exit()
    elif (r.json()["ErrorCode"])==219:
        print ('\033[1;91mYou take before')
        exit()
    elif (r.json()["ErrorCode"])==197:
        print ('\033[1;91mYou take before')
    elif (r.json()["ErrorCode"])==228:
        print ('\033[1;91mYou take before')
        #exit()
    elif(r.json()["ErrorCode"])==10:
        print ("\033[1;91mSomething Wrong, Try again")
        #exit()
    else :
        print ('\033[1;91mSomthing Wrong Try again later')
        #exit()
