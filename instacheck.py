from lxml import html
import requests
import json

def checkpopularity(instausername):
	url = "https://www.instagram.com/" + instausername
	userpage = requests.get(url)
	tree = html.fromstring(userpage.content)
	string = tree.xpath('//script')[6].text
	string = string[21:-1]
	parsed_json = json.loads(string)
	print "Username: ", parsed_json["entry_data"]["ProfilePage"][0]["user"]["username"]
	print "Followers: ", parsed_json["entry_data"]["ProfilePage"][0]["user"]["followed_by"]["count"]
	print "Follows: ",parsed_json["entry_data"]["ProfilePage"][0]["user"]["follows"]["count"]
	print "\n"

def getusername(picurl):
	instaurl = "https://www.instagram.com/p/" + picurl
	instapage = requests.get(instaurl)
	tree = html.fromstring(instapage.content)
	string = tree.xpath('//script')[6].text
	string = string[21:-1]
	parsed_json = json.loads(string)
	instausername = parsed_json["entry_data"]["PostPage"][0]["media"]["owner"]["username"]
	checkpopularity(instausername)


def gethashtag():
	hashtag = raw_input("Which hashtag would you like to search? ")
	url = "https://www.instagram.com/explore/tags/" + hashtag
	page = requests.get(url)
	print "Searching #",hashtag
	tree = html.fromstring(page.content)
	string = tree.xpath('//script')[6].text
	string = string[21:-1]
	#fix the string and make it pretty
	item_dict = json.loads(string)
	picturecount = len(item_dict["entry_data"]["TagPage"][0]["tag"]["media"]["nodes"])
	#get the number of pictures in this page(varies)
	parsed_json = json.loads(string)
	for i in range(picturecount):
		picurl = parsed_json["entry_data"]["TagPage"][0]["tag"]["media"]["nodes"][i]["code"] 
		#prints instagram.com/p/$PICURL
		getusername(picurl)


gethashtag()