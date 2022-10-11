import requests,json
from bs4 import BeautifulSoup as BS
from time import sleep
import sys,os, time, json
import requests as rq 
sleep (1)
print ("\033[1;093mhttps://bestcash2020.com/kvE8")
sleep (1)
Pas=input ("\033[1;092m》Enter The Script Password  :  ")
if Pas!="Abdullah3456":
    print ("\033[1;091mError Password ")
    exit()
else:
	print ()
	sleep (1)
	welcome_message=('\033[1;096mWelcome To Script Orange Gifts By Abdullah\nThe Script Will Add 1000 mg or 500 or 100mg orange')
	for i in welcome_message +"\n":
		sys.stdout.write (i)
		sys.stdout.flush ()
		sleep (0.08)
	Form='''
\033[;091m×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\033[1;092m# By : Abdullah Salah 
# Telegram : https://t.me/Techno0099
# Youtube : https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg
# Facebook : https://www.facebook.com/AbdullahSalah0099
\033[;091m×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

print (Form)


num=input ('\033[1;92m》Enter Number : \033[1;96m')
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
    exit()
elif (r["OfferId"])=="6":
	print ("Try your luck again")
	exit()
#elif (r["OfferId"]=="9"):
	#print ('Congratulations You Have 1000 Mg')
#elif (r["OfferId"])=="8":
    #print ('Congratulations You Have 500 Mg')
elif (r["OfferId"])=="10" or "3" or "2" or "8" or "9" :
    #print ('\033[1;96mCongratulation, You have 100 mg') 



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
	    
'''	elif (r1["ErrorCode"])==219:
	    print ('\033[1;91mYou Took Them Before')
	    exit()
	elif (r1["ErrorCode"])==197:
	    print ('\033[1;91mYou Took Them Before')
	elif (r1["ErrorCode"])==228:
	    print ('\033[1;91mYou Took Them Before')'''
