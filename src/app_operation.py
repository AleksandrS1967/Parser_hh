def app_operation(sp):
    sp.create_db(sp.name_db, sp.password_db)
    sp.create_table(sp.name_db, sp.name_table_employers, sp.command_employers, sp.work_with_db, sp.password_db)
    sp.create_table(sp.name_db, sp.name_table_vacancies, sp.command_vacancies, sp.work_with_db, sp.password_db)
    employers_list = sp.api.get_employers_api(sp.link_hh_employers)
    if employers_list != 0:
        sp.write_data_in_db(employers_list, sp.name_db, sp.work_with_db, sp.name_table_employers,
                            sp.command_insert_employers, sp.name_for_print_employers, sp.password_db)
