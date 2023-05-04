import os
import requests
import uuid
import urllib

from urllib.parse import urljoin
from bs4 import BeautifulSoup

original = "https://kccnceu2023.sched.com/print/"
baseurl = "https://kccnceu2023.sched.com/"

#If there is no such folder, the script will create one automatically
folder_location = r'/Users/pacoxu/git/Python-Webscraping-Program'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(original)
soup= BeautifulSoup(response.text, "html.parser")     
links = soup.find_all("a")
i = 0
for link in links:
    i = i + 1
    if i < 123:
        continue
    url = link.get("href")
    if not url.startswith("event/"):
        continue
    print(str(i) + ") Link:", url, "Text:", link.string)
    response = requests.get(baseurl+url)
    soup2= BeautifulSoup(response.text, "html.parser")  
    for link2 in soup2.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = urllib.parse.unquote(os.path.join(folder_location,link2['href'].split('/')[-1]))
        filenameOnDisk = filename
        if os.path.exists(filename):filenameOnDisk=filename+str(uuid.uuid4())+".pdf"
        with open(filenameOnDisk, 'wb') as f:
            print("write file:", filename)
            f.write(requests.get(urljoin(url,link2['href'])).content)

    for link2 in soup2.select("a[href$='.pptx']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = urllib.parse.unquote(os.path.join(folder_location,link2['href'].split('/')[-1]))
        filenameOnDisk = filename
        if os.path.exists(filename):filenameOnDisk=filename+str(uuid.uuid4())+".pptx"
        with open(filenameOnDisk, 'wb') as f:
            print("write file:", filename)
            f.write(requests.get(urljoin(url,link2['href'])).content)