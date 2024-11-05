import requests
from bs4 import BeautifulSoup

def football_stats():
    url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='TableBase-table')
    rows = table.find_all('tr')[1:21]

   
    print(f"{'Player'} {'GP'} {'RUTD'} {'RETD'} {'PR'} {'KR'} {'INTR'} {'FUMR'}")

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 11:
            player_name = columns[0].text.strip()
            gp = columns[3].text.strip()
            rutd = columns[4].text.strip()
            retd = columns[5].text.strip()
            pr = columns[6].text.strip()
            kr = columns[7].text.strip()
            intr = columns[8].text.strip()
            fumr = columns[9].text.strip()
            print(f"{player_name} {gp} {rutd} {retd} {pr} {kr} {intr} {fumr}")

if __name__ == "__main__":
    football_stats()
