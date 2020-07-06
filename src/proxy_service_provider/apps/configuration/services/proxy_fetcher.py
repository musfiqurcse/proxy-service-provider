import requests
from bs4 import BeautifulSoup
from .selenium_driver import SeleniumDriver
from fake_useragent import UserAgent
import re
import os

import json
class ProxyFetching():


    def __init__(self):
        pass

    def pass_proxy_test(self, proxy_address: str, proxy_port: str, test_url: str, json_res=True):
        try:
            # Initialize User Agent
            # ua = UserAgent()
            concat_proxy_addres = proxy_address + ':'+ proxy_port
            # Initialize Session
            session_proxy = requests.Session()
            # Configure UserAgent()
            # random_ua = ua.random
            # print(random_ua)
            session_proxy.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
            # Configure Proxy
            session_proxy.proxies = {
                'https': 'https://'+concat_proxy_addres
            }
            # Call IP Checker for Proxy Validity
            count = 0
            data = {}
            while count < 3:
                try:

                    # os.system("gsettings set org.gnome.system.proxy.https port '{0}'".format(proxy_port))
                    # os.system("gsettings set org.gnome.system.proxy.https host '{0}'".format(proxy_address))
                    # os.system("gsettings set org.gnome.system.proxy mode 'manual'")
                    res = session_proxy.get(test_url,timeout=10)
                    print(res)
                    if json_res:
                        data = {
                            'output': json.dumps(res.json()),
                            'result': True
                        }
                    else:
                        data = {
                            'output': json.dumps(res.text),
                            'result': True
                        }
                except Exception as ex:
                    data = {'output': str(ex), 'result': False}
                finally:
                    count +=1
                    if data['result'] == True or count >=3:
                        # os.system("gsettings set org.gnome.system.proxy mode 'none'")
                        return data
        except Exception as ex:
            # os.system("gsettings set org.gnome.system.proxy mode 'none'")
            print('Error Occurred while testing proxy')
            return {'output': ex, 'result': False}

    def fetch_data_from_proxy(self,url: str,multi_fetch=False,key_word='?page=',https_check=True):
        # Configure the Selenium Web Driver
        driver = SeleniumDriver()
        # Extrecting Data Using Selenium
        responses = driver.extract_url(url)
        # Parsing The HTML as a Tag Basis using Beautiful Soup
        soup = BeautifulSoup(responses, 'lxml')
        # Initialize the Proxy List
        proxies_list = []
        ip_address = ''
        port = ''
        indexer =  -1
        cols = -1
        port_inclusive = False
        for item in soup.select("table tr"):
            # First td always hold the ip address, hence, we are extracting the first td and removing the unwanted space
            # (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*:?\s*(\d{2,5})
            cond1 = 'elite' in item.text or \
                    'Elite' in item.text or \
                    'ELITE' in item.text or \
                    'yes' in item.text or \
                    'HTTPS' in item.text or \
                    'https' in item.text \
                if not https_check \
                else https_check
            cond2 = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=[^\d])\s*", str(item))
            # cond2 =
            try:
                if cond1 and cond2:
                    if cols > len(item.findAll('td')):
                        continue
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
https://api.ipify.org?format=json
https://httpbin.org/ip
https://ipinfo.io/json
cmd
gsettings set org.gnome.system.proxy.https port '8080'
gsettings set org.gnome.system.proxy.https host '46.4.96.137'
gsettings set org.gnome.system.proxy mode 'manual'
gsettings set org.gnome.system.proxy mode 'none'




"""
