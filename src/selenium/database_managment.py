import mysql.connector
# Root@1234
con = mysql.connector.connect(host="localhost", port=3306, user="root", password="Root@1234", database="amoldb")
curs =con.cursor()
curs.execute("insert into student values (205,'google',106)")
con.commit()
con.close()

print("finished......")