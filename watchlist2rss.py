#!/usr/bin/env python3

import os
from requests import session
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import re
match_imdb = re.compile('^http://www.imdb.com')

def get_feed():
    # required ENV variable: LETTERBOXD_USER
    letterboxd_user = os.environ['LETTERBOXD_USER']

    feedlen = os.environ.get('FEED_LENGTH', 100)
    watchlist_url = f'https://letterboxd.com/{letterboxd_user}/watchlist/'
    output_file = 'feed.xml'
    base_url = 'https://letterboxd.com/'
    page_title = 'Watchlist'

    feed = FeedGenerator()
    feed.title(page_title)
    feed.id(watchlist_url)
    feed.link(href=watchlist_url, rel='alternate')
    feed.description(page_title + ' from Letterboxd')

    s = session()
    page = 0
    total_movies = 0
    while True:
        page += 1
        r = s.get(watchlist_url + '/page/%i/' % page)
        soup = BeautifulSoup(r.text, 'html.parser')

        if page == 1:
            watchlist_title = soup.find('meta', attrs={'property': 'og:title'})
            if watchlist_title is not None:
                page_title = watchlist_title.attrs['content']

        posters = soup.findAll('div', attrs={'class', 'poster'})

        if len(posters) == 0:
            print('No more movies on page %i' % (page, ))
            break
        elif total_movies + len(posters) > feedlen:
            posters = posters[:feedlen-total_movies]

        print('Adding %i movies from page %i' % (len(posters), page))
        total_movies += len(posters)

        for movie in posters:

            movie_page = s.get(base_url + movie.attrs['data-film-slug'])
            movie_soup = BeautifulSoup(movie_page.text, 'html.parser')
            try:
                movie_title = movie_soup.find('meta', attrs={'property': 'og:title'}).attrs['content']
                movie_link = movie_soup.find('a', attrs={'href': match_imdb}).attrs['href']
                movie_link = movie_link[:-11]
            except AttributeError:
                print('Parsing failed')
            movie_description = movie_soup.find('div', attrs={'class': 'truncate'})
            movie_description = movie_description.text.strip()

            item = feed.add_item()
            item.title(movie_title)
            item.description(movie_description)
            item.link(href=movie_link, rel='alternate')
            item.guid(movie_link)

            print(movie_title)

    if total_movies > 0:
        return feed


if __name__ == '__main__':
    get_feed(letterboxd_user).rss_file('feed.xml')
