from bs4 import BeautifulSoup as bs
from pprint import pprint
from pymongo import MongoClient
import json
import re
import requests


class Job():

    def __init__(self, mongodb_uri, db_name, collection_name):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
        self.link_hh = 'https://hh.ru/search/vacancy'

        self.mongodb = MongoClient(mongodb_uri)
        self.db = self.mongodb[db_name]
        self.collection = self.db[collection_name]

    def print_salary(self, salary):
        pass
        # objects = self.collection.find({'salary_max': {'$gt': salary}})
        # for obj in objects:
        #     pprint(obj)

    def search_job(self, vacancy):
        self._parser(vacancy)

    def _parser(self, vacancy):
        params = {
            'text': vacancy, \
            'search_field': 'name', \
            'items_on_page': '100', \
            'page': ''
        }

        html = self._get_html(self.link_hh, params)

        last_page = self._get_last_page_hh(html)

        for page in range(0, last_page):
            params['page'] = page
            html = self._get_html(self.link_hh, params)

            if html.ok:
                parsed_html = self._get_parsed_html(html)

                vacancy_items = parsed_html.find('div', {'data-qa': 'vacancy-serp__results'}) \
                                            .find_all('div', {'class': 'vacancy-serp-item'})
                for item in vacancy_items:
                    vacancy = self._parser_item_hh(item)

                    if self._is_exists('vacancy_link', vacancy['vacancy_link']):
                        self.collection.update_one({'vacancy_link': vacancy['vacancy_link']}, {'$set': vacancy})
                    else:
                        self.collection.insert_one(vacancy)

    def _parser_item_hh(self, item):
        vacancy_data = {}

        # vacancy_name
        vacancy_name = item.find('div', {'class': 'resume-search-item__name'}) \
                            .getText() \
                            .replace(u'\xa0', u' ')

        vacancy_data['vacancy_name'] = vacancy_name

        # company_name
        company_name = item.find('div', {'class': 'vacancy-serp-item__meta-info'}) \
                            .getText() \
                            .replace(u'\xa0', u' ')

        vacancy_data['company_name'] = company_name

        # city
        city = item.find('span', {'class': 'vacancy-serp-item__meta-info'}) \
                    .getText() \
                    .split(', ')[0]

        vacancy_data['city'] = city

        #metro station
        metro_station = item.find('span', {'class': 'vacancy-serp-item__meta-info'}).findChild()

        if not metro_station:
            metro_station = None
        else:
            metro_station = metro_station.getText()

        vacancy_data['metro_station'] = metro_station

        #salary
        salary = item.find('div', {'class': 'vacancy-serp-item__compensation'})

        salary_min = None
        salary_max = None
        salary_currency = None

        if salary:

            salary = salary.getText() \
                            .replace(u'\xa0', u'')

            salary = re.split(r'\s|-', salary)

            if salary[0] == 'до':
                salary_max = int(salary[1])
            elif salary[0] == 'от':
                salary_min = int(salary[1])
            else:
                salary_min = int(salary[0])
                salary_max = int(salary[1])

            salary_currency = salary[-1]
            salary_currency = self._get_name_currency(salary_currency)

        vacancy_data['salary_min'] = salary_min
        vacancy_data['salary_max'] = salary_max
        vacancy_data['salary_currency'] = salary_currency

        # vacancyId
        vacancy_json = json.loads(item.find('script', {'data-name': 'HH/VacancyResponsePopup/VacancyResponsePopup'})['data-params'])

        vacancy_id = vacancy_json['vacancyId']

        # link
        vacancy_data['vacancy_link'] = f'https://hh.ru/vacancy/{vacancy_id}'

        # site
        vacancy_data['site'] = 'hh.ru'

        return vacancy_data

    def _get_last_page_hh(self, html):
        parsed_html = self._get_parsed_html(html)

        if parsed_html:
            page_block = parsed_html.find('div', {'data-qa': 'pager-block'})
            if not page_block:
                last_page = 1
            else:
                last_page = int(
                    page_block.find_all('a', {'class': 'HH-Pager-Control'})[-2] \
                                .getText()
                                )

        return last_page

    def _get_parsed_html(self, html):
        if html.ok:
            parsed_html = bs(html.text,'html.parser')
            return parsed_html

    def _get_html(self, link, params=None):
        html = requests.get(link, params=params, headers=self.headers)
        return html

    def _is_exists(self, name_tags, field):
        return bool(self.collection.find_one({name_tags: { "$in": [field]}}))

    def _get_name_currency(self, currency_name):
        currency_dict  = {
            'EUR': {' €'}, \
            'KZT': {' ?'}, \
            'RUB': {' ?', 'руб.'}, \
            'UAH': {' ?', 'грн.'}, \
            'USD': {' $'}
        }

        name = currency_name

        for item_name, items_list in currency_dict.items():
            if currency_name in items_list:
                name = item_name

        return name