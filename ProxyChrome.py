import requests
from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver

#While Loop Control Variable to Make Sure We Get a Working Proxy
successful_access = False

#Proxy api url
url = "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"

#Gets the api text
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find(text=True)

#Splits the api data into a list of proxies
proxy_list = text.split('\r\n')

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
            chrome.get('https://www.ecosia.org/?c=en')
            #Makes sure the page loaded correctly and the ecosia logo is there
            chrome.find_element_by_xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[1]")
            successful_access = True
            break
        except:
            #If IP Is Too Slow or Not Working, We Continue Down The List
            print("Switching ip")
            chrome.quit()

#Sign Off Message, Letting You Know What Your Public IP is
print("Done. Your Public IP Adress is Now: " + ip)
quit()
