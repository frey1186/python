import pymysql
my_connect = pymysql.connect(host = "127.0.0.1",user = "root",passwd = "root",db="python")

cur = my_connect.cursor()
cur_result = cur.execute("select * from students")

a= cur.fetchall()
print(cur_result)

cur.close()
my_connect.close()