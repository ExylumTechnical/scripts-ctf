
with open("heximage.txt","r") as file:
	line = file.readline()
	while(line!=""):
		print(line[0:2],end="")
		line = file.readline()
