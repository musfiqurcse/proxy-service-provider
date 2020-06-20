import requests
from bs4 import BeautifulSoup
from .selenium_driver import SeleniumDriver
import re


class ProxyFetching():


    def __init__(self):
        pass

    def fetch_data_from_proxy(self,url: str,multi_fetch=False,key_word='?page=',https_check=True):
        driver = SeleniumDriver()
        responses = driver.extract_url(url)
        soup = BeautifulSoup(responses, 'lxml')
        proxies_list = []
        ip_address = ''
        port = ''
        indexer =  -1
        port_inclusive = False
        for item in soup.select("table tr"):
            # First td always hold the ip address, hence, we are extracting the first td and removing the unwanted space
            # (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*:?\s*(\d{2,5})
            cond1 = 'yes' in item.text or 'HTTPS' in item.text or 'https' in item.text if not https_check else https_check
            cond2 = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*", str(item))
            # cond2 =
            cols = -1
            try:
                if cond1 and cond2:
                    if cols > len(item.findAll('td')):
                    select_first_td = str(item.select_one('td').text).strip()
                    cols = len(item.findAll('td'))
                    if indexer == -1:
                        for ik in range(0, cols):
                            if None != item.select_one("td:nth-of-type({0})".format(str(ik))) and re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*", str(item.select_one("td:nth-of-type({0})".format(str(ik))))):
                                indexer = ik
                                if re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*:?\s*(\d{2,5})',str(item.select_one("td:nth-of-type({0})".format(str(ik))).text)):
                                    port_inclusive = True
                                break
                    if port_inclusive:
                        main_data = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*:?\s*(\d{2,5})',
                                  str(item.select_one("td:nth-of-type({0})".format(str(ik))).text))
                        ip_with_port = main_data.group(0)
                        ip_address,port = ip_with_port.split(':')
                    else:
                        ip_address,port = str(item.select_one("td:nth-of-type({0})".format(str(indexer))).text).strip(), str(item.select_one("td:nth-of-type({0})".format(str(indexer+1))).text).strip()
                    if (ip_address, port) not in proxies_list:
                        proxies_list.append((ip_address,port))
                # proxies_list = [':'.join([item.select_one("td").text, item.select_one("td:nth-of-type(2)").text]) for item in
                # if "yes" in item.text]
            except Exception as ex:
                print(ex)
                break
        return proxies_list

"""
Debugging Shell Command
from proxy_service_provider.apps.configuration.services.proxy_fetcher import ProxyFetching
chk = ProxyFetching()
chk.fetch_data_from_proxy('https://www.sslproxies.org/')
https://codereview.stackexchange.com/questions/195842/web-scraping-through-a-rotating-proxy-script
"""
