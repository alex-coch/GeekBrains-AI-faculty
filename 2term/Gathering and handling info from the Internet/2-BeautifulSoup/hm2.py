from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd


def parser_item(item):
    vacancy_date = {}

    it = item.find('a', {'class': 'bloko-link'})
    vacancy_date['vacancy_name'] = it.getText().replace(u'\xa0', u' ')
    vacancy_date['company_name'] = item.find('a', {'class': 'bloko-link bloko-link_kind-tertiary'}) \
        .getText().replace(u'\xa0', u' ')

    salary = item.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary = salary.getText() \
            .replace(u'\xa0', u'')
        salary = re.split(r'\s|-|–', salary)
        for indx,item in enumerate(salary):
            if item == '000':
                salary[indx-1] += salary[indx]
                del(salary[indx])
        salary = [i for i in salary if i != '']
        # print(salary)
        if salary[0] == 'до':
            salary_min = None
            salary_max = int(salary[1])
        elif salary[0] == 'от':
            salary_min = int(salary[1])
            salary_max = None
        else:
            salary_min = int(salary[0])
            salary_max = int(salary[1])
        salary_currency = salary[2]
    vacancy_date['salary_min'] = salary_min
    vacancy_date['salary_max'] = salary_max
    vacancy_date['salary_currency'] = salary_currency

    vacancy_date['vacancy_link'] = it.attrs["href"]
    vacancy_date['site'] = 'hh.ru'
    return vacancy_date


def parser(vacancy, pages):
    vacancy_date = []
    params = {
        'text': vacancy, \
        'search_field': 'name', \
        'items_on_page': '100', \
        'page': ''
        }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
    link = 'https://hh.ru/search/vacancy'

    html = requests.get(link, params=params, headers=headers)
    if html.ok:
        parsed_html = bs(html.text, 'html.parser')
        page_block = parsed_html.find('div', {'data-qa': 'pager-block'})
        if not page_block:
            last_page = '1'
        else:
            last_page = pages

    for page in range(0, last_page):
        params['page'] = page
        html = requests.get(link, params=params, headers=headers)
        if html.ok:
            parsed_html = bs(html.text, 'html.parser')
            vacancy_items = parsed_html.find('div', {'data-qa': 'vacancy-serp__results'})\
                .find_all('div', {'class': 'vacancy-serp-item_redesigned'})

            for item in vacancy_items:
                vacancy_date.append(parser_item(item))
    return vacancy_date


vacancy = input('Enter your vacancy: ')
pages = int(input('Enter the amount of pages (integer): '))
vacancy_date = []
vacancy_date.extend(parser(vacancy, pages))
print(pd.DataFrame(vacancy_date))

