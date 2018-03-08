from Crypto.Cipher import AES
import sys
import getpass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

key = ""
while (len(key) <= 0):
	key = getpass.getpass(bcolors.OKBLUE+'Please enter your key   :'+bcolors.HEADER)
	

IV = ""
while (len(IV) !=16):
	IV = raw_input(bcolors.OKBLUE+"Please enter your IV with 16 chars : "+bcolors.HEADER)

print bcolors.ENDC 
if len(key) < 16 : 
	key = key+" "*(16-len(key))
elif len(key) < 24 :
	key = key+" "*(24-len(key))
elif len(key) < 32 :
	key = key+" "*(32-len(key))
else :
	print "We only could get first 32 chars of your key!  "
	key = key[0:31]

print bcolors.BOLD
print "--> create"
print "--> add"
print "--> read"
print "--> exit"
print bcolors.ENDC

while(True):
	option = raw_input(bcolors.OKBLUE+ "Please enter your option : "+ bcolors.HEADER)
	print "\n"
	if option == "create" :
		rekey = getpass.getpass(bcolors.OKBLUE+"Are you sure ? It deletes encrypted file! Enter your key AGAIN! : "+bcolors.ENDC)
		if len(rekey) < 16 : 
			rekey = rekey+" "*(16-len(rekey))
		elif len(rekey) < 24 :
			rekey = rekey+" "*(24-len(rekey))
		elif len(key) < 32 :
			rekey = rekey+" "*(32-len(rekey))
		else :
			rekey = rekey[0:31]
		if rekey == key : 
			obj = AES.new(key,AES.MODE_CBC,IV)
			ciphertext = obj.encrypt("")
			with open("encrypted.txt", "w") as file:
				file.write(ciphertext)
			print bcolors.WARNING+"[*] encrypted.txt is created"+bcolors.ENDC
	if option == "add":
		obj = AES.new(key,AES.MODE_CBC,IV)
		print bcolors.FAIL + "The format should be  : \nwebsite:username:password" + bcolors.ENDC
		file = open("encrypted.txt","r")
		plaintext = obj.decrypt(file.read())
		#print "file content :"
		#print plaintext
		line = raw_input(bcolors.WARNING +"Please enter your line : "+ bcolors.HEADER)
		plaintext = plaintext + line
		obj = AES.new(key,AES.MODE_CBC,IV)
		ciphertext = obj.encrypt(plaintext+" "*(15-len(plaintext)%16)+"\n")
		file = open("encrypted.txt","w")
		file.write(ciphertext)
		print bcolors.WARNING+"[*] new entry is added "
	if option == "read":
		obj = AES.new(key,AES.MODE_CBC,IV)
		file = open("encrypted.txt","r")
		plaintext = obj.decrypt(file.read())
		print bcolors.OKGREEN + plaintext + bcolors.ENDC
	if option == "help":
		print bcolors.ENDC
		print bcolors.BOLD
		print "--> create"
		print "--> add"
		print "--> read"
		print "--> exit"
		print bcolors.ENDC
	if option == "exit":
		print bcolors.ENDC
		sys.exit(0)

	print "\n"

