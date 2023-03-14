import requests
from bs4 import BeautifulSoup as bs

user_input = input( "enter your github prifile: ")
url = 'https://github.com/' + user_input
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
print(profile_image)