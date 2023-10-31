import requests
from bs4 import BeautifulSoup

def scrape_countries(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    countries = []

    for row in soup.select('.row'):
        for ctr in row.select('.country'):
            country = ctr.select_one('.country-name').text.strip()
            capital_ = ctr.select_one('.country-capital').text.strip()

            country_dict = dict(name = country, capital = capital_)

            countries.append(country_dict)

    return countries

url = 'https://www.scrapethissite.com/pages/simple/'
countries = scrape_countries(url)

print(f'Country\tCapital')
for country in countries:
    print(f'{country["name"]}\t{country["capital"]}')