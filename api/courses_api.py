import requests
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent

def get_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"}
    response = requests.get(url, headers=headers)
    status = response.status_code
    html = response.text
    if status == 200 or str(status)[0] == 3:
        print(f"Код ответа - {status}")
        return html
    else:
        print(f"Ошибка! Код ответа - {status}")

def parse_html(html: str):
    soup = Bs(html, "html.parser")
    value_dollar = soup.find_all("td", class_="t-right")[0].text
    value_euro = soup.find_all("td", class_="t-right")[1].text
    value_yuan = soup.find_all("td", class_="t-right")[2].text
    data = {"dollar": value_dollar,
            "euro": value_euro,
            "yuan": value_yuan}
    return data

URL = "https://www.alta.ru/currency/"
html = get_html(URL)
course_value = parse_html(html)

def get_courses():
    data = [
        {"value": "Доллар", "course_in_rubles": course_value["dollar"],
         "url": "https://www.alta.ru/currency/"},
        {"value": "Евро", "course_in_rubles": course_value["euro"],
         "url": "https://www.alta.ru/currency/"},
        {"value": "Юань", "course_in_rubles": course_value["yuan"],
         "url": "https://www.alta.ru/currency/2"}
    ]
    return data