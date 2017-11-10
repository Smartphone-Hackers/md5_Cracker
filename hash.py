
print("""
               _ ____                        _             
 _ __ ___   __| | ___|    ___ _ __ __ _  ___| | _____ _ __ 
| '_ ` _ \ / _` |___ \   / __| '__/ _` |/ __| |/ / _ \ '__|
| | | | | | (_| |___) | | (__| | | (_| | (__|   <  __/ |   
|_| |_| |_|\__,_|____/   \___|_|  \__,_|\___|_|\_\___|_|  
Smartphone Hackers""")

print ("\n")

import hashlib

m = hashlib.md5()

hash_file = raw_input("Enter Your md5 Hash: ")
wordlist = raw_input("wordlist path: ")

file = open(wordlist,'r')

for line in file:

	m = hashlib.md5()

	line = line.replace("\n","")
	m.update(line)
	file = m.hexdigest()

	if (hash_file == file):
		print("********************************")		
		print("[+] hash valid ",line)
		print("********************************")
		break

	else:
		print ("[-] hash not valid",file)

