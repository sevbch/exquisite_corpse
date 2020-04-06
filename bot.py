import tweepy  # for tweeting
import secrets
from corpse_manager import CorpseManager


def tweet(file):
    corpse = CorpseManager(file)
    sentence = corpse.generate() + " #CadavreExquis"
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)
    auth.secure = True
    print("Posting message: {}".format(sentence))
    api.update_status(status=sentence)


if __name__ == '__main__':
    file = "exquisite_data.csv"
    tweet(file)
