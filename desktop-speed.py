import requests
from requests.models import Response
import json
from bs4 import BeautifulSoup

url = 'sitemapurl'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [myurl.text for myurl in sitemapurls]
for websiteurls in xml_urls:
    strategy = 'desktop'
    api = 'YOUR-API'
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="+websiteurls+"&strategy="+strategy+"&key="+api
    getresponse = requests.get(url)
    js = getresponse.json()
    performance = str (js['lighthouseResult']['categories']['performance']['score']*100)
    fid = js['lighthouseResult']['audits']['max-potential-fid']['displayValue']
    speedindex =  js['lighthouseResult']['audits']['speed-index']['displayValue']
    fcp = js['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
    lcp =  js['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
    cls = js['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
    totalbt = js['lighthouseResult']['audits']['total-blocking-time']['displayValue']
    interactive = js['lighthouseResult']['audits']['interactive']['displayValue']