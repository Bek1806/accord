
import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    base_url = 'https://m.mashina.kg'
    soup = BS(html, 'html.parser')
    tabs = soup.find('div', class_='search-results-table')
    if not tabs:
        print("Таблица результатов поиска не найдена.")
        return []
    
    posts = tabs.find_all('div', class_='list-item list-label')
    posts = tabs.find_all('div', class_='list-item list-label')
    if not posts:
        print("Посты не найдены.")
        return []

    for post in posts:
        title = post.find('div', class_='block title').text.strip()
        price = post.find('div', class_='block price').text.strip()
        description = post.find('div', class_='block info-wrapper item-info-wrapper').text.strip()
        
        # Удаляем лишние пробелы и пустые строки
        description = ' '.join(description.split())
        price = ' '.join(price.split())

        # Извлекаем URL изображения (только первое изображение)
        picture_tag = post.find('img')
        picture_url = picture_tag['src'] if picture_tag else 'Нет изображения'

        # Извлекаем ссылку (href) и формируем полную ссылку
        link_tag = post.find('a')
        link_url = base_url + link_tag['href'] if link_tag else 'Нет ссылки'

        print(f"Название: {title}\nЦена: {price}\nОписание: {description}\nИзображение: {picture_url}\nСсылка: {link_url}\n{'-'*60}\n")
    
    return posts




def save_txt(data, filename = 'accordbishkek'):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write('title, price, description')
        for item in data:
             f.write("\t".join(item) + "\n")
    print(f"Data saved to {filename}")





def main():
    URL = 'https://m.mashina.kg/search/all/'
    html = get_html(URL)
    if html:
        get_links(html)
    else:
        print("Не удалось получить HTML.")

if __name__ == '__main__':
    main()