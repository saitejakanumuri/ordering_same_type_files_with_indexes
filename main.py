import requests
from bs4 import BeautifulSoup as bs

t_user = input("input user handle: ")
url= 'https://twitter.com/'+t_user
r=requests.get(url)
soup=bs(r.content,'html.parser')
profile_photo=soup.find('img',{'alt':'Profile photo'})
print(profile_photo)
