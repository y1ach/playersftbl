import requests
from bs4 import BeautifulSoup
import time

def scrape_team(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        
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

    except requests.exceptions.RequestException as e:
        return f"HTTP hatası: {str(e)}"
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"
