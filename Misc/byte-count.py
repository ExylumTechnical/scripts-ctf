with open("data.txt","r") as file:
	data=int(file.readline());
	total=0;
	while data!="":
		total=total+data
		try:
			data=int(file.readline());
		except:
			print("end of file")
			break
	print(total)
