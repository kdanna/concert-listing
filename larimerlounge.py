# import libraries
import urllib2
import logging
from bs4 import BeautifulSoup

class LarimerLoungeShows(object):

    def __init__(self, venue_name, venue_url):
        self.venue_name = venue_name
        self.venue_url = venue_url

    # make beautiful soup
    def getBSObject(self):
        # query the website and return the results to a new variable
        page = urllib2.urlopen(self.venue_url).read()
        # use BeautulSoup to parse the html and store its contents into a new variable
        soup = BeautifulSoup(page, 'html.parser')
        # this will create a BS concert section object that is iterable
        concerts = soup.find_all('div', attrs={'class': "list-view-item"})
        return concerts
        

    #  create list of lists contain each concert event from BS
    def getConcertListings(self):
        all_concert_listings = [] # create a master list of all the concert event listings from sing_concert_listing
        for concert in self.getBSObject():
            try:
                single_concert_listing = []  # create a concert list for each event
                single_concert_listing.append(self.venue_name)
                headliner = concert.find('h1', attrs={'class': 'headliners summary'}).text.strip()
                single_concert_listing.append(headliner)
                opening_act = concert.find('h2', attrs={'class': 'supports description'}).text.strip()
                single_concert_listing.append(opening_act)
                date = concert.find('h2', attrs={'class': 'dates'}).text.strip()
                single_concert_listing.append(date)
                ticket_price = concert.find('h3', attrs={'class': 'price-range'}).text.strip()
                single_concert_listing.append(ticket_price)

                all_concert_listings.append(single_concert_listing)
            except Exception as e:
                logging.info('exception raised, but passed so program will run: %s' % e )
                pass
        return all_concert_listings
