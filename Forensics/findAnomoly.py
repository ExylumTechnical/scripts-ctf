from collections import Counter

suspectUsers=open("suspected.csv","w")

with open("log - sorted.csv","r") as file:
	line = file.readline()
	line_split=line.split(",");
	name=line_split[0]
#	current_success=line_split[3]
	anomolies=[]
	check_buffer=[]
	while(line!=""):
# put each username into thier own
# anomolous behaviour criteria different IP addresses, successive failed login attempts
		if(line_split[0]==name):
			check_buffer.append(line_split)
			line = file.readline()
			line_split=line.split(",");
		else:
			ip_addrs=[]
			success=[]
			for i in check_buffer:
				ip_addrs.append(i[1])
				success.append(i[3])
				
#				print(i)
#			print("differing IP addresses: ",end="")
			ip_counter = Counter(ip_addrs);
			ip_count = len(ip_counter)
			success_counter = Counter(success)
			success_count = len(success_counter)
			
			if(ip_count > 1 and success_count > 1):
				for i in check_buffer:
					suspectUsers.write(i[0]+","+i[1]+","+i[2]+","+i[3])
					

#				for i in range(len(check_buffer)):
#					if(i>0):
#						if( check_buffer[i][3] == "No" and check_buffer[i-1][3]=="Yes" ):
#							print(check_buffer[i])
#					print(i[0]+" "+i[1]+" "+i[2]+" "+i[3][:-1]+" ")

			check_buffer=[]
			name=line_split[0]
			line = file.readline()
			line_split=line.split(",");




suspectUsers.close()
