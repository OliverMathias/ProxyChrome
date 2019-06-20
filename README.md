# ProxyChrome

## Flowchart
![Flowchart](./images//ProxyChromeFlowChart.png)
## Table of contents
* [Flowchart](#flowchart)
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This simple program pulls a fresh list of 'elite' level anonymous proxies from [Proxy-List](https://www.proxy-list.download) via their API. Then it checks the list for a non-crowded proxy and opens an [Ecosia](https://www.ecosia.org/) search page in Chrome.

## Technologies
Project is created with:
* Python 3.6
* BeautifulSoup4
* Selenium
* Chromium

## Setup
To run this project, install the following programs:

* Python 3.x.x (https://www.python.org/)
* Google Chrome (https://www.google.com/chrome/)
* Chrome Driver (https://sites.google.com/a/chromium.org/chromedriver/)

Then run these four lines to install the ProxyChrome dependencies:
```
$ pip install requests
$ pip install beautifulsoup4
$ pip install lxml
$ pip install selenium
```
Enjoy your anonymous browsing experience!
