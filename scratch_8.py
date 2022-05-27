#database wrinting using pymysql
import pymysql as p

db = p.connect(host='localhost', user='root', passwd='anuroop1602', database='timepass')

a = db.cursor()
a.execute("Show databases")
print("\n ***This is my database list****")
for i in a:
    print(i)
a.execute("insert into  values('m',76,88)")

a.execute("commit")

print("\n***This is my table data***")

a.execute("select* from details")
for i in a:
    print(i)

