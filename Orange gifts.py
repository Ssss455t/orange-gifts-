import requests,json
import requests as rq 
from bs4 import BeautifulSoup as BS
from time import sleep
import sys,os, time, json
print ('\033[1;92mclick on this link to get password👇')
print ()
link="\033[1;93mhttps://bestcash2020.com/kvE8"
print (link)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
if password !="Abdullah3456":
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

c=rq.get ('https://excretive-oaks.000webhostapp.com/AbdullahSalah_Ctv&Htv.php').json()

ctv=(c['ctv'])
htv=(c['htv']) 


url="https://backend.orange.eg/api/WheelOfFortune/CheckEligibility"

headers={
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

json={
"ServiceClassID":"1045","channel":{"ChannelName":"MobinilAndMe",
"Password":"ig3yh*mk5l42@oj7QAR8yF"},
"Dial":f"{num}",
"IsEasyLogin":False,
"Lang":"ar",
"Password":f"{pas}"
}

r=requests.post (url,headers=headers,json=json).json()
c=(r["OfferId"])
if (r["ErrorCode"]==9):
    print ('\033[1;91mError Number Or Password')
    exit()
elif (r["ErrorCode"]==16):
    print ('\033[1;91mError ctv Or htv')
    exit()
elif (r["OfferId"])=="" and (r["ErrorCode"])==218:
    print ('\033[1;91mAttempts are Over , Try Tomorrow')
    exit()
elif (r["ErrorCode"])==219:
    print ('\033[1;96mYou Took them before, Try After Some Days')
elif (r["OfferId"])=="6":
	print ("Try your luck again")
elif (r["OfferId"]=="9"):
	print ('Congratulations You Have 1000 Mg')
elif (r["OfferId"])=="8":
    print ('Congratulations You Have 500 Mg')
elif (r["OfferId"])=="10" or "3" or "2":
    print ('\033[1;96mCongratulation, You have 100 mg') 



######################################


cc=rq.get ('https://excretive-oaks.000webhostapp.com/AbdullahSalah_Ctv&Htv.php').json()

ctv1=(cc['ctv'])
htv1=(cc['htv'])


url1="https://backend.orange.eg/api/WheelOfFortune/Offerfulfillment"

json1={
"OfferID":f"{c}",
"ServiceClassID":"1044","channel":{"ChannelName":"MobinilAndMe",
"Password":"ig3yh*mk5l42@oj7QAR8yF"},
"Dial":f"{num}",
"IsEasyLogin":"false",
"Lang":"ar",
"Password":f"{pas}"
}


headers1={
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


r1=requests.post(url1,headers=headers1,json=json1).json()
if (r1["ErrorCode"])==0:
    print ('\033[1;96mDone Added Megabytes')
elif (r1["ErrorCode"])==9:
    print ('\033[1;91mError Number Or Password')
    exit()
elif(r1["ErrorCode"])==10:
    print ("\033[1;91mSomething Wrong, Try again")
else :
    print ('\033[1;91mSomthing Wrong Try again later')
