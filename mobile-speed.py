import requests
from requests.models import Response
import json
from bs4 import BeautifulSoup
import csv 

url = 'sitemapurl'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [myurl.text for myurl in sitemapurls]
for websiteurls in xml_urls:
    strategy = 'mobile'
    api = 'YOUR-API'
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="+websiteurls+"&strategy="+strategy+"&key="+api
    getresponse = requests.get(url)
    js = getresponse.json()
    mperformance = str (js['lighthouseResult']['categories']['performance']['score']*100)
    mfid = js['lighthouseResult']['audits']['max-potential-fid']['displayValue']
    mspeedindex =  js['lighthouseResult']['audits']['speed-index']['displayValue']
    mfcp = js['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
    mlcp =  js['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
    mcls = js['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
    mtotalbt = js['lighthouseResult']['audits']['total-blocking-time']['displayValue']
    minteractive = js['lighthouseResult']['audits']['interactive']['displayValue']