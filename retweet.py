import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.


auth = tweepy.OAuthHandler('SZg2GdKeb0G0BVj5dSujfzM94', '4xXr6eZRDqqBgGrNHfu7V4uyRztPZoD1rBM44zBuiyTvQ13kge')
auth.set_access_token('1278599604947173377-OxL2W1NTvGR7LQtT5zk0kmDR0L3lFx', '8jm4C7aoHsuJaQ4mpjlsEMPzGBZr3ilD4WJdYpEP9TTGB')
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='#COVID19India').items(9999):
    try:
        print('\nClancy found tweet by @' +
              tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')

        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        sleep(120)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
