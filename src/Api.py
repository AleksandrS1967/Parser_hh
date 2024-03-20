import json
import requests


class Api:

    @staticmethod
    def get_employers_api(link):
        """получает работодателей, группирует в нужном виде"""
        params = {
            "per_page": 10,
            "sort_by": "by_vacancies_open"
        }
        try:
            response = requests.get(link, params)
            res = json.loads(response.text)['items']
            res_list = []
            for i in res:
                res_list.append([i['id'], i['name'], i['alternate_url'], i['open_vacancies']])
            return res_list
        except (Exception, requests.exceptions.ConnectionError) as error:
            print(error)
            return 0

    def get_vacancies_from_company_api(self, id_, link, count_vacancies):
        """получает вакансии, группирует в нужном виде"""
        params = {
            "per_page": count_vacancies,
            "employer_id": id_
        }
        try:
            response = requests.get(link, params)
            res = json.loads(response.text)['items']
            res_list = []
            for i in res:
                salary = self.get_salary(i)
                res_list.append(
                    [i['id'], i['name'].lower(), salary, i['alternate_url'], i['employer']['id'],
                     i['employer']['name']])
            return res_list
        except (Exception, requests.exceptions.ConnectionError) as error:
            print(error)
            return 0

    @staticmethod
    def get_salary(item):
        """проверяет наличие данных"""
        if item['salary'] != None:
            if item['salary']['from']:
                salary = item['salary']['from']
                return salary
            else:
                salary = item['salary']['to']
                return salary
        else:
            return 0
