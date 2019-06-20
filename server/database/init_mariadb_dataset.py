import mysql.connector as mariadb


try:
    mariadb_connection = mariadb.connect(host='mariadb', user='test', password='test', database='wanted')
    cursor = mariadb_connection.cursor()

    cursor.execute("""
        insert into company (name_ko, name_en, name_ja, tag_ko, tag_en, tag_ja) 
        values (%s, %s, %s, %s, %s, %s)
    """, ('원티드랩',
          'Wantedlab',
          '',
          '태그_4|태그_20|태그_16',
          'tag_4|tag_20|tag_16',
          'タグ_4|タグ_20|タグ_16'))
    mariadb_connection.commit()
except mariadb.Error as mce:
    print(mce)
