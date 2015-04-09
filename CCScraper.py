from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

#URLs of pages we are interested in
BASE_URL = "http://talk.collegeconfidential.com/college-admissions/"
url2 = "http://talk.collegeconfidential.com/financial-aid-scholarships/"

#Grabs titles from College Confidential forum pages.
def get_titles(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    postList = soup.find("table", "DataTable DiscussionsTable")
    titles = [a.string for a in postList.findAll("a", "Title")]
    return titles
	
#Takes in a list and outputs it to .csv format	
def csv_writer(data):
        with open('titles.csv', 'wb') as f:
         writer = csv.writer(f, delimiter = ',')
         rows = zip(data)
         for row in rows:
          writer.writerow(row)

		  		  

csv_writer(get_titles(url2))


