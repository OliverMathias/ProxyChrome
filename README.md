# ProxyChrome

## Table of contents
* [General info](#general-info)
* [Flowchart](#flowchart)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This simple program pulls a fresh list of 'elite' level anonymous proxies from [Proxy-List](https://www.proxy-list.download) via their API. Then it checks the list for a non-crowded proxy and opens an [Ecosia](https://www.ecosia.org/) search page in Chrome.

## Flowchart
![Flowchart](./images//ProxyChromeFlowChart.png)

## Technologies
Project is created with:
* Python 3.6
* BeautifulSoup4
* Selenium 3.14
* Chrome 74.0.37

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
Browser anonymously WHILE planting trees! :deciduous_tree:
