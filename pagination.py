import httpx
import requests
from bs4 import BeautifulSoup

def scrape_teams(url: str) -> None:
    max_pages = 6
    current_page = 1
    
    while current_page <= max_pages:
        current_url = f'{url}?query=&amp;sort_direction=desc&amp;sort=rate&amp;page={current_page}'
        print(current_url)
        
        raw_html = requests.get(current_url)
        
        print(raw_html.status_code)
        
        current_page += 1
        
    

def main() -> int:
    url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2'
    # url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2'
    # url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=2'
    # url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=3'
    scrape_teams(url)
    return 0

if __name__ == '__main__':
    exit(main())