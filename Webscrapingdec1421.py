import requests

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Human_rights"
resp = requests.get(url)
resp.status_code
h = resp.text
s = BeautifulSoup(h,"html.parser")
s
s.h1.text
#s.u1.text
s.title.text

li_data = s.findAll('li')
li_data[11].text

li_text = []

df = open("/Users/purnimagebhardt/Desktop/webscrape/li_wiki_hr.txt","a",encoding="utf-8")
for i in range(len(li_data)):
    li_text.append(li_data[i].text)
    df.write(str(li_data[i].text))
df.close()

#Amazon Reviews

url1 = "https://www.amazon.in/OnePlus-Nord-Charcoal-128GB-Storage/product-reviews/B09576CYNP?reviewerType=all_reviews"

for i in range(1,6):
    rev_res = requests.get(url1+str(i))
    if rev_res.status_code ==200:
        print("Connection Successful")
    else:
        print("Connection Failed")



rev_res = requests.get(url1+str(i))
rev_data = rev_res.text
rev_soup = BeautifulSoup(rev_data,'html.parser')
revs = rev_soup.findAll('span',attrs={"data-hook":"review-body"})
revs[0].text