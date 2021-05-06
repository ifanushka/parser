import requests
from bs4 import BeautifulSoup
import csv

host = 'https://minfin.com.ua'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
try:
    k = int(input('Сколько страниц нужно спарсить?(max - 30): '))
    if (k > 0) and (k < 31):
        with open('data.csv','a',newline='') as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerow(['Title','Link','Name of Bank','Info'])
            for i in range(1,k+1):
                writer.writerow(['Page ',i])
                url = f'https://minfin.com.ua/cards/catalog?page={i}&per-page=10'
                resp = requests.get(url, headers=HEADERS)
                soup = BeautifulSoup(resp.content, 'html.parser')
                divs = soup.find_all('div', class_='row')
                for div in divs:
                    title= div.find('div',class_='title').get_text(strip=True)
                    href = host + div.find('div',class_='title').find('a').get('href')
                    n_bank= div.find('div', class_='brand').get_text(strip=True)
                    info = div.find('div', class_='excerpt').find('ul').get_text(strip=True)
                    writer.writerow([title,href,n_bank,info])
    else: print('Такой странички нет(')
except:
    print('Что-то сломалось.')
    