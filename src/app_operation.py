def app_operation(sp):
    sp.create_db(sp.name_db, sp.password_db)
    sp.create_table(sp.name_db, sp.name_table_employers, sp.command_employers, sp.work_with_db, sp.password_db)
    print('222')