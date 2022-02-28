import httpx
from bs4 import BeautifulSoup
from core.urlcore import *

def scrape_teams(url: str) -> None:
    max_pages = 6
    current_page = 1
    
    proxies = {"all": "socks5://127.0.0.1:9050"}
    while current_page <= max_pages:
        current_url = f'{url}?query=&amp;sort_direction=desc&amp;sort=rate&amp;page={current_page}'
        print(current_url)
        
        
        raw_html = httpx.get(current_url,)
        
        print(raw_html.status_code)
        
        current_page += 1
        
    

def main() -> int:
    url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2'
    scrape_teams(url)
    return 0

if __name__ == '__main__':
    exit(main())