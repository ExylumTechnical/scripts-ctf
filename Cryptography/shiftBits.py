## Used in PicoCTF in 2025
## will shift bits in a file named enc by 8

with open('enc','r') as file:
	flag=file.read();
#	print(enctext)
	for i in range(0,len(flag),2):
		print((ord(flag[i]) << 8)+ ord(flag[i])+1,end="")


#	''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
