'''

Problem: An application to lookup the top trending topics in Twitter

Implementation: An application to find the top ten trending topics.

@author: Saud Bin Habib

'''

#Imports
import twitter
import argparse
import os


def extract_available_countries(twitter_api: twitter) -> list:
    '''

    :param twitter_api: this method takes twitter object
    :return: returns list of available countries and their ids as a set.
    '''

    available_trends = twitter_api.trends.available()
    return [(trend['name'].lower(), trend['woeid']) for trend in available_trends]


def twitter_trends(country: str, top: int, twitter_api: twitter) -> list:
    '''

    :param country: it takes country as a str
    :param top: it takes top as number integer.
    :param twitter_api: it takes the twitter api object
    :return: and returns the list of top trends of this specific country.
    '''

    available_trends = extract_available_countries(twitter_api)
    woeid = [trend[1] for trend in available_trends if trend[0] == country]
    if woeid:
        place_trends = twitter_api.trends.place(_id=woeid[0])
        return [trend['name'] for trend in place_trends[0]['trends'][:top]]
    return []


def entrypoint():
    '''
    This is the function which will be called by the console script to print the top trends of country.
    '''

    parser = argparse.ArgumentParser(description='Argument Parser for the twitter trends.')
    parser.add_argument('--country', type=str, required=True)
    parser.add_argument('--top', type=int, default=10)

    args = parser.parse_args()
    country = str(args.country).lower()
    top = int(args.top)

    CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
    OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN')
    OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET')

    auth = twitter.oauth.OAuth(
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET,
        CONSUMER_KEY,
        CONSUMER_SECRET
    )

    twitter_api = twitter.Twitter(auth=auth)
    top_trends = twitter_trends(country, top, twitter_api)
    if top_trends:
        for counter, trend in enumerate(top_trends):
            print(counter, ') ' + trend)
    else:
        print('There is no Trend for your entered value.')
