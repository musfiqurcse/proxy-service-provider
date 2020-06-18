import requests
from bs4 import BeautifulSoup



class ProxyFetching():


    def __init__(self):
        pass

    def fetch_data_from_proxy(self,url: str,multi_fetch=False,key_word='?page='):
        responses = requests.get(url)
        print(responses.text)
        soup = BeautifulSoup(responses.text, 'lxml')
        for item in soup.select("table.table tr"):
            # First td always hold the ip address, hence, we are extracting the first td and removing the unwanted space
            select_first_td = str(item.select_one('td').text).strip()
            cut = select_first_td
        proxies_list = [':'.join([item.select_one("td").text, item.select_one("td:nth-of-type(2)").text]) for item in
                    if "yes" in item.text]
        return proxies_list

