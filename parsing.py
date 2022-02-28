#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-02-28 21:57:37
# @Author  : zzz <easy-quest@vk.com>
# @Link    : https://github.com/easy-quest/
# @Version : 1.0.0
import httpx
from bs4 import BeautifulSoup
from click import secho as echo
from core.pwcore import *

url = "http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/1"

querystring = {"query":"","region_id":"806","subregion_id":"0","price[min]":"","price[max]":"","unit":"g","weight[min]":"","weight[max]":"","type":"momental"}

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    'referer': "http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/1",
    'connection': "keep-alive",
    'upgrade-insecure-requests': "1",
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "same-origin",
    'sec-fetch-user': "?1",
    'cache-control': "max-age=0"
    }  

cookies = {
    'pregate': "1646068570.39e0d0c6765fc4e8c009a0f5dbe862bc.2e0f25f14562f061dd7fd2c2a33fc1e4", 
    'gate': "1646068591.253c8d72ea0bedf45400473203b45c8e.880653c8c540b21f503efa0d974c50f2", 
    '_session': "eyJpdiI6IjQ0U0RPSFg4M0owdUJTNG5hSEcrb0E9PSIsInZhbHVlIjoiZDhrSCtoZnFVRkEzdnRsM3JzdUZ6eTVPMnh6TTZaR2VMY0o0eDA3U1Q2N09JUFpOYWJQVkpIa3dZR2MyN1dtTCIsIm1hYyI6IjNkZWVmZGQwNDBmMTBjYjAxZDI5NDUyZDg1NzA3M2Y4YjQ4ZGU1NjE0YmFmYjRhZjkwZTQ2OTQ2MDJiNWM0ZGEifQ%3D%3D",
    'upc': "eyJpdiI6IlNLS1dRM0UyVDhmSU1aMmpcLzdRcFdRPT0iLCJ2YWx1ZSI6IitzdFFNM2hCTlhJclNDYXhoZFdaa3Z3d0JXU3RFQWRiSXlQVTNjZFkxZGs9IiwibWFjIjoiOTBiZTAzZjNkMTQxZDE5MTUzOWQxODI1NDRlMGNmOWQ2ZGQ2ZTE5NDk0YjhiZGNiYzBmZjRiYWU1ZjEzNzUyNSJ9", 
    'r1': "1646068653800"
    }

timeout = httpx.Timeout(10.0, connect=60.0)

with httpx.Client(proxies='socks5://127.0.0.1:9050') as hs:
# with httpx.Client(proxies=proxies) as hs:
    r = hs.get(url, headers=headers, params=querystring, cookies=cookies, timeout=timeout) 
    soup = BeautifulSoup(r.content, 'lxml')

    with open("./html/" + ft() + ".html", 'w') as f: f.write(soup.prettify())
    items = soup.find_all('div', class_='catalog_item')
    
    itemsReegion = soup.find('li', class_='over').text
    # print(f'{itemsReegion}')
    echo(f'{itemsReegion}',bg='blue')
    
    for n, i in enumerate(items, start=1):
        itemName = i.find('div', class_='title').text.strip()
        itemPrice = i.find('span').text.strip()
        print(f'{n}: {itemName} {itemPrice} ')