# Used to decrypt a piece of text by adding and subtracting from values
encryptedText="Eyooirtnrpincd spiiiect e mv"
encryptedTextLen=len(encryptedText)
print()
for i in range(0,int(encryptedTextLen),2):
	print((ord(encryptedText[i])+ord(encryptedText[i+1])-120), end=" ")
print()


print()
for i in range(0,int(encryptedTextLen)):
	print((ord(encryptedText[i])-32), end=" ")
print()

def shiftDown(encryptedText):
	print("Attempting to subtract values")
	for i in range(100):
		for j in range(5):
			try:
				print(chr(ord(encryptedText[j])-i), end=" ")
			except:
				print("",end="")
		print()
def shiftUp(encryptedText):
	print("Attempting to add values")
	for i in range(100):
		for j in range(5):
			try:
				print(chr(ord(encryptedText[j])+i), end=" ")
			except:
				print("",end="")
		print()
	
	

