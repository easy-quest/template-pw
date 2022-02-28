import httpx
from bs4 import BeautifulSoup

def scrape_teams(url: str) -> None:
    max_pages = 24 
    current_page = 1
    
    while current_page <= max_pages:
        print(f'{url}?page_num={current_page}')
        
        current_page += 1
    
def main() -> int:
    url = 'http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2'
    scrape_teams(url)
    return 0

if __name__ == '__main__':
    exit(main())