from src.app_operation import *
from src.functions import *
from src.WorkWithDb import *

name_db = 'hh_db'
password_db = '1234'
work_with_db = WorkWithDb()
name_table_employers = 'employers'
command_employers = 'employer_id int UNIQUE primary key, employer_name text, employer_url text, open_vacancies int'