import requests
from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver

#While Loop Control Variable to Make Sure We Get a Working Proxy
successful_access = False

#Pulls the HTML of Our Proxy Website
website_url = requests.get("https://free-proxy-list.net/").text
#Makes a Soup Variable That Turns Raw HTML Into "Parse-able" Data
soup = BeautifulSoup(website_url,"lxml")
#Puts The Table Object Into The "table" Variable
table = soup.find("tbody")
#Puts all Rows In The Table Variable Into the "rows" Variable
rows = table.find_all("tr")

#Initializes an Empty List for All Proxies
proxy_list = []

#For Each Row in Our List of Rows, We Extract The IP Number and Port, Appending Them To Our List Of IPs
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text for ele in cols]
    ip = cols[0]
    port = cols[1]
    fullip = ip + ":" + port
    proxy_list.append(fullip)

#This While Loop Will Continue Attempting to Open a DuckDuckGo Search Page With The Proxies From Our List Until It Succeeds
while successful_access == False:
    for ip in proxy_list:
        try:
            #This Block Initializes The Chrome Browser With a Proxy
            print("Trying Proxy:" + ip)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % ip)

            #This Block Attempts to Open a New Chrome Tab Using The Proxy and If Successful, Quits The Script
            chrome = webdriver.Chrome(options=chrome_options)
            chrome.get('https://duckduckgo.com/')
            successful_access = True
            break
        except:
            #If IP Is Too Slow or Not Working, We Continue Down The List
            print("Switching ip")
            chrome.quit()

#Sign Off Message, Letting You Know What Your Public IP is
print("Done. Your Public IP Adress is Now: " + ip)
quit()
