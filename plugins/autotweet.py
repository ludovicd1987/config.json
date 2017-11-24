from utils import *

print ('loading ' + __name__)

def action(bot, update):
	tweets= ""
	tweet_id = re.findall(r'/status/+(\d*)', update.message.text)
	try:
		status = api.get_status(tweet_id[0], tweet_mode='extended')
		tweet = status.full_text
		favs = str(status.favorite_count)
		RTs = str(status.retweet_count)
		user = status.user.screen_name
		url = treatLink("https://twitter.com/" + user)
		username = status.user.name
	except:
		pass
	try:
		try:
			quoted_tweet = status.quoted_status["text"]
			quoted_user = status.quoted_status["user"]["screen_name"]
			quoted_username = status.quoted_status["user"]["name"]
			url = treatLink("https://twitter.com/" + quoted_username)
			update.message.reply_text("`_______quoted tweet_______`\n  [" + quoted_username + " - @" + quoted_user + "](" + url + ")\n" + quoted_tweet + "`\n_____end of quoted tweet_____`\n\n`RTs:{" + RTs + "} | Likes: " + favs + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			if len(tweet) < 110:
				update.message.reply_text("[" + username + " - @" + user + "](" + url + ")" + "\n`RTs:" + RTs + " | Likes: " + favs +"`", parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
			else:
				update.message.reply_text("[" + username + " - @" + user + "](" + url + ")\n" + tweet + "\n`RTs:" + RTs + " | Likes: " + favs + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
	except:
		pass

info = {	'triggers' 	:	r'.*http[s]?://twitter\.com.+/status/\d+.*',
			'active'	: 	True,
			'admin'		: 	False}