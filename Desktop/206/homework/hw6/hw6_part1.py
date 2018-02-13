# 507/206 Homework 6 Part 1
import requests
from bs4 import BeautifulSoup

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here
html = requests.get('http://newmantaylor.com/gallery.html').text
soup = BeautifulSoup(html, 'html.parser')
searching_div = soup.find_all('img')


for cat in searching_div:
    try:
        print (cat['alt'])
    except:
        print ("No alternative text provided!")

print()
