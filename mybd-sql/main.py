import mysql.connector
from mysql.connector import Error
from function import execute_read_query, connection

# sql = "INSERT INTO hats (title, price, category) VALUES(%s, %s, %s)"
# sql = "SELECT * FROM `orders` JOIN `users` ON users.userId = 1"

# sql = "SELECT * from users"
# # myCur.executemany(sql)
# myCur.execute(sql)
#
# for el in myCur:
#     print(el)

select_users = "SELECT users.login FROM `orderds` JOIN `users` ON orderds.userId = users.id"
select_items = "SELECT items.title FROM `orderds` JOIN `items` ON orderds.itemId = items.id;"
sql = execute_read_query(connection, select_users)
sql1 = execute_read_query(connection, select_items)

for user in sql:
    for succeeding in user:
        print(succeeding, end="")
        print(" - ")
    for item in sql1:
        print(item, "")
