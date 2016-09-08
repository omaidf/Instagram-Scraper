from lxml import html
import requests
import json

#part one: Given a URL, access the page and parse the output and show username, followers, follows.
url = "insert IG URL here"
page = requests.get(url)
tree = html.fromstring(page.content)
string = tree.xpath('//script')[6].text
string = string[21:-1]
parsed_json = json.loads(string)
print "Username: ", parsed_json["entry_data"]["ProfilePage"][0]["user"]["username"]
print "Followers: ", parsed_json["entry_data"]["ProfilePage"][0]["user"]["followed_by"]["count"]
print "Follows: ",parsed_json["entry_data"]["ProfilePage"][0]["user"]["follows"]["count"]
#next: parse User_ID's from search feed, feed URL's and automate.