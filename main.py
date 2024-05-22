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
    container = soup.find('div', class_='search-results-table')
    if not container:
        print("Таблица результатов поиска не найдена.")
        return []
    
    
    posts = container.find_all('div', class_='list-item list-label')
    
    for post in posts:
        title = post.find('div', class_='block title').text.strip()
        price = post.find('div', class_='block price').text.strip()
        describe = post.find('div', class_='block info-wrapper item-info-wrapper').text.strip()
        describe = ' '.join(describe.split())
        price = ' '.join(price.split())
        link_tag = post.find('a')
        link_url = base_url + link_tag['href'] if link_tag else 'Нет ссылки'

        print(f"Название: {title}\nЦена: {price}\nОписание: {describe} \nСсылка: {link_url}\n{'-'*60}\n")
    
    return posts

def save_txt(data, filename='output.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('название\tцена\tописание\n')  
        for item in data:
            f.write("\t".join(item) + "\n")  
    print(f"Данные сохранены в файл {filename}")

# Пример использования:
# data = [
#     ["Название1", "Цена1", "Описание1"],
#     ["Название2", "Цена2", "Описание2"]
# ]
# save_txt(data)

        
        
        
 

    
def main():
    URL = 'https://m.mashina.kg/search/honda/accord/?generation=752&region=1&town=2'
    html = get_html(URL)
    if html:
        get_links(html)
    else:
        print("Не удалось получить HTML.")

if __name__ == '__main__':
    main()