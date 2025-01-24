import requests
from bs4 import BeautifulSoup

def scrape_team(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table_div = soup.find('div', {'id': 'yw1'})
        
        if table_div:
            rows = table_div.find_all('tr')

            headers = rows[0].find_all('th')
            headers_text = [header.get_text(strip=True) for header in headers]

            data = []
            for row in rows[1:]:
                cols = row.find_all('td')
                cols_text = [col.get_text(strip=True) for col in cols]
                data.append(cols_text)
            
            return {"headers": headers_text, "data": data}
        else:
            return "Tablo bulunamadı!"
    else:
        return f"Sayfaya erişim başarısız: {response.status_code}"
