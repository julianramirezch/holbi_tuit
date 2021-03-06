#!/usr/bin/python3

import tweepy
import requests
from lxml import html


def tuit_decision(dec):
    """ Check user decision"""
    while dec != 'y' and dec != 'n':
        dec = input('Yes or No? (y/n)')
    return dec


def get_news_link():
    """ Get First news link """
    print('1. HackerNews')
    print('2. The Verge')
    user_portal = input('Select your portal (1, 2): ')
    while not user_portal.isnumeric():
        user_portal = input('Select your portal (1, 2): ')

    # HackerNews Selection
    if int(user_portal) == 1:
        r = requests.get("https://news.ycombinator.com/best")
        webpage = html.fromstring(r.content)
        links = webpage.xpath('//a/@href')

        print('1. {}'.format(links[11]))
        print('2. {}'.format(links[17]))
        print('3. {}'.format(links[23]))

        user_selection_link = input('Select your link (1, 2, 3,): ')
        while not user_selection_link.isnumeric():
            user_selection_link = input('Select your link (1, 2, 3): ')

        if int(user_selection_link) == 1:
            return(str(links[11]))
        elif int(user_selection_link) == 2:
            return(str(links[17]))
        elif int(user_selection_link) == 3:
            return(str(links[23]))
        else:
            print('ERROR: Choose 1, 2, 3')
            return('')

    # Wired Selection
    if int(user_portal) == 2:
        r = requests.get("https://www.wired.com/")
        webpage = html.fromstring(r.content)
        links = webpage.xpath('//a/@href')

        print('1. {}'.format(links[55]))
        print('2. {}'.format(links[56]))
        print('3. {}'.format(links[57]))
        print('4. {}'.format(links[58]))
        print('5. {}'.format(links[59]))
        print('6. {}'.format(links[60]))
        print('7. {}'.format(links[61]))

        user_selection_link = input('Select your link (1, 2, 3, 4, 5, 6, 7): ')
        while not user_selection_link.isnumeric():
            user_selection_link = input('Select your link (1, 2, 3, 4, 5, 6, 7): ')

        if int(user_selection_link) == 1:
            return(str(links[55]))
        elif int(user_selection_link) == 2:
            return(str(links[56]))
        elif int(user_selection_link) == 3:
            return(str(links[57]))
        elif int(user_selection_link) == 4:
            return(str(links[58]))
        elif int(user_selection_link) == 5:
            return(str(links[59]))
        elif int(user_selection_link) == 6:
            return(str(links[60]))
        elif int(user_selection_link) == 7:
            return(str(links[61]))
        else:
            print('ERROR: Choose 1, 2, 3, 5, 6, 7')
            return('')


def holbi_tuit():
    """ Send tuit """
    consumer_key = 'YOUR CONSUMER KEY'
    consumer_key_secret = 'YOUR CONSUMER KEY SECRET'
    access_token = 'YOUR ACCESS TOKEN'
    access_token_secret = 'YOUR ACCESS TOKEN SECRET'
    link = get_news_link()
    message = 'Hi, this is Holbi tuit \U0001F916 ! I was created to tweet every day. I use the news portal https://news.ycombinator.com/ or https://www.wired.com/ this is the top news: '
    tuit = message + '\n' + link
    print('Today Tuit:')
    print(tuit)
    print('Characters: {}'.format(len(tuit)))

    user_selection = tuit_decision(input('Do you want to do this tweet?(y/n): '))
    if user_selection is 'y':
        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api.update_status(tuit)
    else:
        print('-' * 20, end='\n')
        holbi_tuit()


if __name__ == "__main__":
    print('Hi , I\'m Holbi Tuit \U0001F916')
    holbi_tuit()
