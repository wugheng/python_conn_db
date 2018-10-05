import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='826209886', database='sqltest')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user2 (id, name) values (%s, %s)', ('1', 'Tom'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user2 where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()