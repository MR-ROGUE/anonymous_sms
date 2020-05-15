import requests, os, sys, time
print("\033[96mCoded by github.com/Sanif007 \033[0m ")
print("\033[93m Version 2.0 \033[0m")
print("\033[91m Checking dependencies... \033[0m")
time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("\033[91m1.\033[0m \033[92mSend anonymous sms\033[0m")
    print("\033[91m2.\033[0m \033[92mCheck status of sms\033[0m")
def control() :
    ctrl = input("What you want to do : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    else :
        print("\033[91mInvalid number\033[0m")
def sms() :
   phone_no = input("enter phone number : ")
   msg = input("message to send : ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })

   print(resp.text)
   if '"success" : true' in resp.text :
       print('Msg delivered! ')
   if '"success" : false' in resp.text :
       print("failed to send msg!\n Sorry!! Try again!! ")
def status() :
  textID = input("Enter textID of sms : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
os.system("clear")
os.system("toilet -f mono12 -F gay Scammer ")
print("\033[96mCoded by github.com/Sanif007")
print("Insta handle - @haoi_hackers_academy_of_india")
menu()
control()
