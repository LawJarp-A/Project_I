#Auth: Prajwal_anagani
#LawJarp_a

#import required libraries
import requests
import bs4
import sys
import math

#Set some global variables

#Can change so to retrieve more of less posts
no_of_posts = 5

#Put your own usr agent
usr = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

headers = {'User-agent':usr}
print("Got you user-agent: ",usr)

#Function used to get posts(duh)
def get_posts(t, top_no, headers):

	#Download the subreddit info
    data_req = requests.get("https://www.reddit.com/"+t+"/", headers = headers)

    #Check if subreddit is valid
    if not (data_req.status_code == requests.codes.ok):
    	print("Invalid subreddit. Exiting program..")
    	sys.exit(0)

	#Parse it to bs4 format
    data = bs4.BeautifulSoup(data_req.text,'html.parser')

	#Get the no_of_posts required
    tops = data.find_all(class_="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3")[0:top_no]

	#
    d = {}
	#Enumerate and handle the different types of posts
    for i, l in enumerate(tops):
        a = l.find(class_="_eYtD2XCVieq6emjKBH3m").text

        b = "UNKNOWN TYPE"

        try:
			#Image post
            b = l.find(alt='Post image')['src']
        except:
            try:
				#Gif Post
                b = l.find("video").find("source")['src']
            except:
                try:
					#Imgur link
                    b = l.find(class_ = "styled-outbound-link")['href']
                    if(b[0]=="/"):
                        b = "https://www.reddit.com"+b

                except:
                    try:
						#Link to discussion
                        b = "https://www.reddit.com"+l.find(class_ = "SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")['href']
                    except:
                        pass

		#Goto the comments page
        c_url = l.find("a")['href']

		#Get web info and parse it to bs4 format
        data_req = requests.get(c_url, headers = headers)
        data = bs4.BeautifulSoup(data_req.text,'html.parser')

		#Find and gather the top 5 comments
        k = data.find_all(class_ = "_3cjCphgls6DH-irkVaA0GM")[0:5]

		#Get the text part from the HTML tags
        k = list(map(lambda x: x.text, k))

		#Return dictionar with the format {Title_name:(Link,list of top 5 comments)}
        d[a] = (b,k)

		#print("%d %" %(math.floor((((i+1)/top_no))*100)))


    return d

#Get and display
sr = input("Enter subreddit (format: 'r/sub'): ")
tp = get_posts(sr, 5, headers)
for i in tp.keys():
    print("Title: ",i)
    print()
    print("Image/Gif/dicussion: ", tp[i][0])
    print()
    print("Top 5 comments:")
    for k in tp[i][1]:
        print("-->",k)
    print()
    print()
