import hashlib
import sys
wordlist = open("sky-wordlist.txt","w")

for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				plainstrong=str(sys.argv[1]+str(a)+str(b)+str(c)+str(d))
				strong=plainstrong.encode('utf-8')
				wordlist.write(plainstrong+"\n")
wordlist.close()
