import time
import requests
from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

print(r"""

  _____                      _____ _
 |  __ \                    / ____| |
 | |__) | __ _____  ___   _| |    | |__  _ __ ___  _ __ ___   ___
 |  ___/ '__/ _ \ \/ / | | | |    | '_ \| '__/ _ \| '_ ` _ \ / _ \
 | |   | | | (_) >  <| |_| | |____| | | | | | (_) | | | | | |  __/
 |_|   |_|  \___/_/\_\\__, |\_____|_| |_|_|  \___/|_| |_| |_|\___|
                       __/ |
                      |___/
                                                    V-1.1
""")

def getProxies():
    print()
    print("Fetching Proxy list...")
    print()

    #Proxy api url
    url = "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"

    #Gets the api text
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find(text=True)

    #Splits the api data into a list of proxies
    proxy_list = text.split('\r\n')

    for proxy in proxy_list:
        print(proxy)

    print()
    print("Proxies Fetched: ", len(proxy_list))

    #An easy way for the user to quit both windows
    print()
    quit = input("Enter any Key to Quit: ")

#This is the main ProxyChrome function
def main():
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
                # and tests it in headless to make sure the proxy ip works
                print()
                print("Trying Proxy:" + ip)
                chrome_options = webdriver.ChromeOptions()
                #This line removes the dev tools message for the trying block
                chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                chrome_options.add_argument('--proxy-server=%s' % ip)
                chrome_options.add_argument('--headless')

                #This Block Attempts to Open a New Chrome Tab Using The Proxy in headless, and If Successful,
                # Continues on to Open a regular browser for the user
                chrome = webdriver.Chrome(options=chrome_options)
                chrome.get('https://www.ecosia.org/?c=en')

                #Makes sure the page loaded correctly and the ecosia logo is there
                chrome.find_element_by_xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[1]")

                #If the script has gotten this far it means that the ecosia logo has loaded and
                chrome_options = webdriver.ChromeOptions()

                #This line allows the script to continue on even before
                # the browser has fully loaded the page
                caps = DesiredCapabilities().CHROME
                caps["pageLoadStrategy"] = "none"

                #This line removes the dev tools message for the trying block and
                # adds our now valid IP to browser
                chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                chrome_options.add_argument('--proxy-server=%s' % ip)
                chrome = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)
                chrome.get('https://www.ecosia.org/?c=en')

                successful_access = True
                break

            except:
                #If IP Is Too Slow or Not Working, We Continue Down The List
                print()
                print("Proxy Blocked, Switching Proxy")
                chrome.quit()

    #Sign Off Message, Letting You Know What Your Public IP is
    print("Opening Browser, Your Public IP Adress is Now: " + ip)
    print()

    #An easy way for the user to quit both windows
    quit = input("Enter any Key to Quit: ")

if __name__ == "__main__":
    main()
    #getProxies()
