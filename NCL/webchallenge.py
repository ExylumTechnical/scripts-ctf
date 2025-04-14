import requests
import json


def simpleRequest(url):
	# GET request
	try:
		response = requests.get(url)
	except:
		print("Exception recieved")

	# Check if the request was successful (status code 200)
	if response.status_code == 200:
	    data = response.json()  # Parse JSON response
	    return data
	else:
	    print(f"Error: {response.status_code}")

def simplePost(url,value):
	# POST request
#	url = "https://example.com/api/submit"
#	data = {"key1": "value1", "key2": "value2"}
	data = {"answer":value}
	response = requests.post(url, json=data)

	if response.status_code == 200:
	    print("Data submitted successfully")
	    print(response.json())
	else:
	    print(f"Error: {response.status_code}")
# store the URLs
targetURL_Wordlist="https://<random hex number sequence>-wordly.web.cityinthe.cloud/static/words.json";
targetURL_Submission="https://<random hex number sequence>-wordly.web.cityinthe.cloud/check";
targetURL_Seed="https://<random hex number sequence>-wordly.web.cityinthe.cloud/seed";

# get the wordlist, grab the seed value, parse the json, get the seed, generate the key, find the word, and dump the flag.
wordlist=simpleRequest(targetURL_Wordlist)
seedvalue=((simpleRequest(targetURL_Seed)))
seedJsonDump=json.dumps(seedvalue)
seedJsonLoad=json.loads(seedJsonDump)
seedValue=int(seedJsonLoad["seed"]);
correctWord=wordlist[(seedValue*4)%len(wordlist)];
print(correctWord)
print(simplePost(targetURL_Submission,correctWord))
