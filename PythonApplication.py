import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#Have user enter url, where to put the data (i.e. D:\Test, and what extension you want to look for (.pdf, .xlsx, etc...)
url = input("Paste URL: ")
folder_location = input("Enter filepath: ")
extension = input("Enter file extension you are trying to capture: ")

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")   
links = soup.findAll('a')
user_links = [url + link['href'] for link in links if link['href'].endswith(extension)]

soup= BeautifulSoup(response.text, "html.parser")   

#look for link ending in user provided extension
for link in soup.select("a[href$='{}']".format(extension)):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
        
