import pymysql


conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='python')

cur = conn.cursor()

reCount = cur.execute('insert into students(name,sex,age,tel) '
                      'values(%s,%s,%s,%s)',('erin','man',"19","1239124934"))


conn.commit()

cur.close()
conn.close()

print(reCount)
