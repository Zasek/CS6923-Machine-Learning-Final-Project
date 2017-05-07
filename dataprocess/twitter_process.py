import csv
import pandas as pd
import sys
import string
import simplejson as json
from twython import Twython

t = Twython(app_key='',
	    app_secret='',
	    oauth_token='',
	    oauth_token_secret='')

ids = "3017099491, 4776235117, 802158585966919680, 27636553, 847720063, 252903217, 70819324, \
       839497464365350913, 698970824838139908, 828094155314315264, 756999150516834308, \
       764196865885794305, 826213214685913088, 3317314489, 749412914197516288, \
       729996828813352961, 750629505752977408, 3257695526, 4848045286, 754256194588598272, \
       4861803504, 812651473062526976, 816377498623610880, 288979145, 224383150, \
       569559818, 581817134, 764084202, 28878121, 390583023, 829274309235527680, \
       2737823912, 761424990143074304, 3154613740, 3049845738, 708177228127817728, \
       3033319478, 3039547217, 3077727070, 730155897008193536, 737254164791734273, \
       736609915939131392, 735819642690621440, 731793461616115713, 753793982350655488, \
       745203881798426626, 833580614485938176, 749015749163876352, 715800615054663680, \
       740064325574877184, 57588181, 47624365, 236999725, 4348237453, 243905905, \
       166739404, 133880286, 4895514574, 26861418, 1202561, 8605462, 82006140, \
       818989320342151168, 27251422, 86315276, 15425787, 128295889, 18153494, 3249981810, \
       89195501, 33820269, 582454742, 17822926, 461998155, 14158807, 114690248, 80522018, \
       219471857, 2856459903, 1572082038, 3498661753, 581241318, 2499228050, 242663173, \
       228614375, 128620022, 19561116, 2330646224, 395978320, 1213854728, 3401145215, \
       2817717320, 1529273749, 2751270469, 3810742695, 139557376, 14338147, 243856880, \
       133501277, 793077200"

fields = ['id', 'id_str', 'screen_name', 'location', 'description' , 'url', 'followers_count', 'friends_count', 'listed_count', 
	  'created_at', 'favourites_count', 'verified', 'statuses_count', 'lang', 'status', 'default_profile',
	  'default_profile_image', 'has_extended_profile', 'name', 'bot']
users = t.lookup_user(user_id = ids)

statusarray = {}
for i in range(99):
	try:
		statusarray[i] = str(users[int(i)]['status'])
	except KeyError:
		pass


data = dict()	
s = 0
for inx, entry in enumerate(users):
	r = {}
	for f in fields:
		r[f] = ""
	r['id'] = entry['id']
	r['id_str'] = entry['id_str']
	r['screen_name'] = entry['screen_name']
	r['location'] = entry['location']
	r['description'] = entry['description']
	r['url'] = entry['url']
	r['followers_count'] = entry['followers_count']
	r['friends_count'] = entry['friends_count']
	r['listed_count'] = entry['listed_count']
	r['created_at'] = entry['created_at']
	r['favourites_count'] = entry['favourites_count']
	r['verified'] = entry['verified']
	r['statuses_count'] = entry['statuses_count']
	r['lang'] = entry['lang']
	r['default_profile'] = entry['default_profile']	
	r['default_profile_image'] = entry['default_profile_image']
	r['has_extended_profile'] = entry['has_extended_profile']
	r['name'] = entry['name']
	if s < 50:
		r['bot'] = 1
	else:
		r['bot'] = 0
	try:
		r['status'] = statusarray[inx]
	except KeyError:
		pass
	data[s] = pd.Series(r, index=fields)
	s = s+1


frame = pd.DataFrame(data)
frame.transpose().to_csv("twitterentities.csv", index=False)



#pd.to_csv("twitterentities.csv")

#a = csv.writer(open("twitterentities.csv", "wb"))
#a.writerows(["id", "id_str", "screen_name"])

