<img src="images/proxychrome.png" align="right" />

# ProxyChrome          

## 🚩 Table of contents
* [General info](#general-info)
* [Flowchart](#flowchart)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This simple program pulls a fresh list of 'elite' level anonymous proxies from [Proxy-List](https://www.proxy-list.download) via their API. Then it checks the list for a non-crowded proxy and opens an :earth_americas:[Ecosia](https://www.ecosia.org/) search page in Chrome.

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

## 💾 Setup
Clone this repository:
```
https://github.com/OliverMathias/ProxyChrome
```

Then run this line to install the ProxyChrome dependencies:
```
$ pip install -r dependencies.txt
```

Finally, cd into the folder and run ProxyChrome:
```
$ python3 ProxyChrome.py
```
Browser anonymously WHILE planting trees!
:seedling: :evergreen_tree: :deciduous_tree:


## Acknowledgments
* [Ecosia](https://www.ecosia.org/)
* [Proxy-List](https://www.proxy-list.download)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
