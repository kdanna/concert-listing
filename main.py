# import libraries
import urllib2
from bs4 import BeautifulSoup


# test one url to scrape concert listings and then add the others in the array

# specify the url
venue_page = 'http://www.hi-dive.com/'

'''use urllib2 to get the html page for the vendue_page url. 
Query the website and return the results to a new variable'''
page = urllib2.urlopen(venue_page).read()

# use BeautulSoup to parse the html and store its contents in a new variable
soup = BeautifulSoup(page, 'html.parser')

# now it's time to extract the listings data I want to keep by finding the right tag and indentifying attrs
# find venue name
venue_name = soup.title.string.strip()
print 'venue_name: ', venue_name

# find headliner name
headliner_name_box = soup.find('h1', attrs={'class': 'headliners summary'})
headliner_name = headliner_name_box.a.string  # find the <a> child tag and grab out the text using the .string method
print 'headliner_name: ', headliner_name

# find concert openers
supporting_name_box = soup.find('h2', attrs={'class': 'supports description'})
supporting_name = supporting_name_box.a.string
print 'supporting_names: ', supporting_name

# find concert date
concert_date = soup.find('h2', attrs={'class': 'dates'}).string
print 'concert date: ', concert_date

# find concert price
ticket_price = soup.find('h3', attrs={'class': 'price-range'}).string.strip()
print 'ticket price: ', ticket_price

