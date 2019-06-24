import csv

import mysql.connector as mariadb


try:
    mariadb_connection = mariadb.connect(host='mariadb', user='test', password='test', database='wanted')
    cursor = mariadb_connection.cursor()

    with open('wanted_temp_data.csv', 'r') as csv_file:
        companies = csv.DictReader(csv_file)

        cursor.execute("TRUNCATE TABLE company")
        for company in companies:
            cursor.execute("""
                insert into company (name_ko, name_en, name_ja, tag_ko, tag_en, tag_ja) 
                values (%s, %s, %s, %s, %s, %s)
            """, (company['company_ko'],
                  company['company_en'],
                  company['company_ja'],
                  company['tag_ko'],
                  company['tag_en'],
                  company['tag_ja']))
    mariadb_connection.commit()
except mariadb.Error as mce:
    print(mce)
