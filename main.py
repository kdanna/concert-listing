# import libraries
import sys
import urllib2
import csv
import logging
from bs4 import BeautifulSoup

from hidive import HiDiveShows
from larimerlounge import LarimerLoungeShows

# sett system default encoding as utf-8 so that all strings are encoded using that
reload(sys)
sys.setdefaultencoding('utf-8')


def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
        level=logging.INFO)
    log = logging.getLogger()


def main():

    logging.info('program starting')

    # instance of hiDiveShows class and pass in name and website url
    hi_dive = HiDiveShows('hi-dive', 'http://www.hi-dive.com/')
    hi_dive.getBSObject()
    hd_all_concert_listings = hi_dive.getConcertListings()

    # instance of larmierLounge class. pass in name and website url
    larimer_lounge = LarimerLoungeShows('larimer-lounge', 'http://www.larimerlounge.com/')
    larimer_lounge.getBSObject()
    ll_all_concert_listings = larimer_lounge.getConcertListings()
    # print ll_all_concert_listings

    # open a csv file and write out concert contents
    with open('hi-dive-listings.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file,  delimiter = ',')
        writer.writerows(hd_all_concert_listings)
        writer.writerows(ll_all_concert_listings)

        logging.info('rows written to csv. program complete')


if __name__ == '__main__':

    setup_logging()
    main()