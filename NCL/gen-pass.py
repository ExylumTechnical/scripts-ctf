import hashlib

for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				plainstrong=str("SKY-SENH-"+str(a)+str(b)+str(c)+str(d))
				strong=plainstrong.encode('utf-8')
				print(hashlib.md5(strong).hexdigest() + " : "+plainstrong)
