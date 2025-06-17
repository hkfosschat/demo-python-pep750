#!/usr/bin/env python3


# 使用 f-string 處理資料庫 SQL 字串

# 正常輸入
id = 123
email = "a123@school.edu.hk"
sql = f"SELECT * FROM students WHERE id={id} AND email={email} LIMIT 1";
print(type(sql))
print(sql)

# SQL injection 示範
# 參考：https://xkcd.com/327/
# 詳細：https://en.wikipedia.org/wiki/SQL_injection
id = 123
email = "'; DELETE * FROM students; SELECT 1"
sql = f"SELECT * FROM students WHERE id={id} AND email={email} LIMIT 1";
print(type(sql))
print(sql)


# 使用舊 syntax 配合 sqlescapy 套件處理 SQL injection 問題
from sqlescapy import sqlescape

# 逐個變量使用 SQL escape
id = sqlescape(id)
email = sqlescape(email)
safe_sql = f"SELECT * FROM students WHERE id={id} AND email={email} LIMIT 1";
print(type(safe_sql))
print("安全的 SQL：   %s" % safe_sql)
print("不安全的 SQL： %s" % sql)
