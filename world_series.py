import requests
from bs4 import BeautifulSoup

def world_series_data():
    url = 'https://en.wikipedia.org/wiki/List_of_World_Series_champions'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='wikitable')

    print(f"{'Year'} {'Winning Team'} {'Manager'} {'Series'} {'Losing Team'}")

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        
        if len(columns) >= 5:
            year = columns[0].get_text(strip=True)
            winning_team = columns[1].get_text(strip=True)
            manager = columns[2].get_text(strip=True)
            series = columns[3].get_text(strip=True)
            losing_team = columns[4].get_text(strip=True)
            print(f"{year} {winning_team} {manager} {series} {losing_team}")

if __name__ == "__main__":
    world_series_data()
