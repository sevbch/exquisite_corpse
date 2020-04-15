import tweepy  # for tweeting
import secrets
from corpse_manager import CorpseManager


def tweet(data):
    corpse = CorpseManager(data_pickle=data)
    sentence = corpse.generate()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)
    auth.secure = True
    print("Posting message: {}".format(sentence))
    api.update_status(status=sentence)


if __name__ == '__main__':
    file = 'data_pickle'
    tweet(file)
