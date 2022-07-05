import requests
from bs4 import BeautifulSoup


def task() -> dict:
    url = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'
    cyrillic_upper = [(lambda c: chr(c))(i) for i in range(1040, 1072)]
    cyrillic_letters = {letter: 0 for letter in cyrillic_upper}
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        animals = soup.find('div', class_='mw-category mw-category-columns').find_all('li')
        next_page = "https://ru.wikipedia.org" + soup.find('a', title="Категория:Животные по алфавиту", text='Следующая страница').get("href")
        url = next_page
        for animal in animals:
            if animal.text[0] in cyrillic_letters.keys():
                cyrillic_letters[animal.text[0]] += 1
            if animal.text[0] == 'A':
                return cyrillic_letters


if __name__ == '__main__':
    result = task()
    for key, value in result.items():
        print(f"{key}: {value}")
