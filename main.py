# import libraries
import urllib2
import csv
import logging
from bs4 import BeautifulSoup


def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
        level=logging.INFO)
    log = logging.getLogger()


def main():

    logging.info('program starting')

    # test one url to scrape concert listings
    venue_page = 'http://www.hi-dive.com/'

    # query the website and return the results to a new variable
    page = urllib2.urlopen(venue_page).read()

    # use BeautulSoup to parse the html and store its contents into a new variable
    soup = BeautifulSoup(page, 'html.parser')

    # this will create a BS concert section object that is iterable
    concerts = soup.find_all('div', attrs={'class': "list-view-item"})
    # print concert_details[0].prettify() 

    all_concert_listings = [] # create a master list of all the concert event listings from sing_concert_listing
    for concert in concerts:
        try:
            single_concert_listing = []  # create a concert list for each event
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

    # open a csv file and write out concert contents
    with open('hi-dive-listings.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file,  delimiter = ',')
        writer.writerows(all_concert_listings)

        logging.info('rows written to csv. program complete')


if __name__ == '__main__':

    setup_logging()
    main()  