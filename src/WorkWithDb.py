import psycopg2


class WorkWithDb:
    @staticmethod
    def create_db(name_db, password_db):
        """создаёт базу данных"""
        try:
            conn = psycopg2.connect(database="postgres",
                                    user="postgres",
                                    password=password_db,
                                    host="localhost")
            cur = conn.cursor()
            conn.autocommit = True
            cur.execute(f'create database {name_db}')
            print(f'База данных {name_db} успешно создана')
            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def connect_db(name_db, password_db):
        """подключается к базе данных и возвращает курсор и коннект"""
        try:
            conn = psycopg2.connect(database=name_db,
                                    user="postgres",
                                    password=password_db,
                                    host="localhost")
            cur = conn.cursor()
            conn.autocommit = True
            return cur, conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def get_companies_and_vacancies_count(work_with_db, name_db, password_db):
        """получает список всех компаний и количество вакансий у каждой компании"""
        cur, conn = work_with_db.connect_db(name_db, password_db)
        cur.execute(f"select employer_name, open_vacancies from employers")
        data = cur.fetchall()
        print('\nполучаем список всех компаний и количество вакансий у каждой компании..:')
        for i in data:
            print(f'Название - {i[0]} | кол-во открытых вакансий - {i[1]}')
        cur.close()
        conn.close()

    @staticmethod
    def get_all_vacancies(work_with_db, name_db, password_db):
        """получает список вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        cur, conn = work_with_db.connect_db(name_db, password_db)
        cur.execute(f"select employer_name, vacancy_name, salary, vacancy_url from vacancies")
        data = cur.fetchall()
        print(
            '\nполучаем список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию..:')
        for i in data:
            print(
                f'Название компании - {i[0]} | название вакансии - {i[1]} | зарплата - {i[2]} | ссылка на вакансию - {i[3]}')
        cur.close()
        conn.close()

    @staticmethod
    def get_avg_salary(work_with_db, name_db, password_db):
        """получает среднюю зарплату по вакансиям"""
        cur, conn = work_with_db.connect_db(name_db, password_db)
        cur.execute(f"select employer_name, avg(salary) from vacancies group by employer_name")
        data = cur.fetchall()
        print('\nполучаем среднюю зарплату по вакансиям..:')
        for i in data:
            print(f'Название компании - {i[0]} | средняя зарплата по вакансиям - {int(i[1])}')
        cur.close()
        conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary(work_with_db, name_db, password_db):
        """получаеn список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        cur, conn = work_with_db.connect_db(name_db, password_db)
        cur.execute(
            f"select vacancy_name, salary, vacancy_url from vacancies where salary > (select avg(salary) from vacancies)")
        data = cur.fetchall()
        print('\nполучаем список всех вакансий, у которых зарплата выше средней по всем вакансиям..:')
        for i in data:
            print(f'Название вакансии - {i[0]} | зарплата - {int(i[1])} | ссылка на вакансию - {int(i[1])}')
        cur.close()
        conn.close()

    @staticmethod
    def get_vacancies_with_keyword(work_with_db, name_db, password_db, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        cur, conn = work_with_db.connect_db(name_db, password_db)
        cur.execute(f"select vacancy_name, salary, vacancy_url from vacancies where vacancy_name like '%{keyword}%'")
        data = cur.fetchall()
        print('\nполучаем список всех вакансий, в названии которых содержатся переданные в метод слова..:')
        for i in data:
            print(f'Название вакансии - {i[0]} | зарплата - {int(i[1])} | ссылка на вакансию - {int(i[1])}')
        cur.close()
        conn.close()
