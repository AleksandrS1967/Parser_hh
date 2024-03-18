from src.app_operation import *
from src.functions import *
from src.WorkWithDb import *
from src.Api import *

name_db = 'hh_db'
password_db = '1234'
link_hh_employers = 'http://api.hh.ru/employers'
link_hh_vacancies = 'http://api.hh.ru/vacancies'
work_with_db = WorkWithDb()
api = Api()
name_table_employers = 'employers'
name_table_vacancies = 'vacancies'
name_for_print_employers = 'работодателей'
name_for_print_vacancies = 'вакансий'
command_employers = 'employer_id int UNIQUE primary key, employer_name text, employer_url text, open_vacancies int'
command_vacancies = 'vacancy_id int UNIQUE primary key, vacancy_name text, salary int, vacancy_url text, employer_id int, employer_name text, description text, constraint fk_vacancies_eployers foreign key(employer_id) references employers(employer_id)'
command_insert_employers = '(employer_id, employer_name, employer_url, open_vacancies) values (%s, %s, %s, %s)'