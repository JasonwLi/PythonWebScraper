import urllib2
import json
from collections import OrderedDict
from sys import exit
from bs4 import BeautifulSoup

j = {}
j['Companies'] = []
## 10 pages
for i in range(1,11):
    link ="http://data-interview.enigmalabs.org/companies/?page=" + str(i)
    ## opening page
    try:
        page = urllib2.urlopen(link)
    except:
        print "error in opening page " + str(i)
        pass
    ## getting invidual components of html page
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class': 'table table-hover'})
    body = table.find('tbody')
    rows = body.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        sublink = cols[1].find('a').get('href')
        sublink = "http://data-interview.enigmalabs.org"+sublink
        ## modifying link to include %20 for whitespaces
        sublink = sublink.replace(' ', '%20')
        company_page = urllib2.urlopen(sublink)
        soup = BeautifulSoup(company_page, 'html.parser')
        ## putting table data into a list of a lists
        table_data = [[cell.text for cell in row("td")]
                                 for row in soup("tr")]
        ## converting list to json with fields in original order
        j['Companies'].append(json.dumps(OrderedDict(table_data)))
## output json file
with open('solution.json', 'w') as sol:
    json.dump(j, sol)
print j

