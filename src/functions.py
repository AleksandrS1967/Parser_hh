import psycopg2


def create_table(name_db, name_table, command, work_with_db, password_db):
    """создаёт таблицу"""
    cur, conn = work_with_db.connect_db(name_db, password_db)
    try:
        cur.execute(f'create table {name_table} ({command})')
        print(f'Таблица {name_table} успешно создана')
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        cur.close()
        conn.close()
        print(error)


def write_data_in_db(employers, name_db, work_with_db, name_table, command, name_for_print, password_db):
    """наполняет таблицу данными"""
    cur, conn = work_with_db.connect_db(name_db, password_db)
    for i in employers:
        try:
            cur.execute(
                f"insert into {name_table} {command}",
                i)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    print(f"Таблица {name_table} успешно наполнена данными {name_for_print}")
    cur.close()
    conn.close()
