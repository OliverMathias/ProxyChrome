<img src="images/proxychrome.png" align="right" />

# ProxyChrome          
<a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://pypi.org/project/beautifulsoup4/">
    	<img src="https://img.shields.io/badge/built%20with%20-BS4-green.svg" />
    </a>

## General info
This simple program pulls a fresh list of 'elite' level anonymous proxies from [Proxy-List](https://www.proxy-list.download) via their API. Then it checks the list for a non-crowded proxy and opens an :earth_americas:[Ecosia](https://www.ecosia.org/) search page in Chrome.

## 🚩 Table of contents
* [General info](#general-info)
* [Sample](#sample)
* [Flowchart](#flowchart)
* [Technologies](#technologies)
* [Setup](#setup)

## Sample
![](http://g.recordit.co/6BhKNS7vRj.gif)

## Flowchart
![Flowchart](./images//ProxyChromeFlowChart.png)

## Technologies
Project is created with:
* Python 3.6
* BeautifulSoup4
* Selenium 3.14
* Chrome 74.0.37

## Prerequisites
* Python 3.x.x (https://www.python.org/)
* Google Chrome (https://www.google.com/chrome/)
* Chrome Driver (https://sites.google.com/a/chromium.org/chromedriver/)

#### **Make sure to Download Compatible Versions of Chrome Driver and Chrome**


## 💾 Setup
Clone this repository:
```
https://github.com/OliverMathias/ProxyChrome
```

Then run this line to install the ProxyChrome dependencies:
```
$ pip install -r dependencies.txt
```

Make sure to copy your 'chromedriver' file into the ProxyChrome folder:

![](http://g.recordit.co/rcMJLz2inT.gif)

Finally, cd into the folder and run ProxyChrome:
```
$ python ProxyChrome.py
```
Browse anonymously WHILE planting trees!
:seedling: :evergreen_tree: :deciduous_tree:


## Acknowledgments
* [Ecosia](https://www.ecosia.org/)
* [Proxy-List](https://www.proxy-list.download)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
