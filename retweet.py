import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.


auth = tweepy.OAuthHandler('Insert your  auth codes here both token and secret')
auth.set_access_token('insert access token code', 'insert access token secret')
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='#keyword content you want to retweet').items(999):
    try:
        print('\n Username found tweet by @' +
              tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')
        # no of times the bot should search for hashtags of the keyword is written inside items
        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        sleep(200)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
