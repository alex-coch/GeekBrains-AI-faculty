from utils import Job
from pprint import pprint


vacancy_db = Job('mongodb://192.168.1.11:27017/', 'vacancy', 'vacancy_db')
vacancy_db.print_salary(100_000)

vacancy_db.collection.update_one({'vacancy_link': 'https://hh.ru/vacancy/50931935'},
                                 {'$set': {'city':'Москва', 'company_name':'EGGHEADS'}})
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)
vacancy = 'Python'
vacancy_db.search_job(vacancy)
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)