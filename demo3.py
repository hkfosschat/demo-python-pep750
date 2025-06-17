#!/usr/bin/env python3


# 使用 function 加上 Template String syntax 及 sqlescapy 套件處理 SQL injection 問題
# 簡化代碼改善可讀性
from sqlescapy import sqlescape
from string.templatelib import Template, Interpolation

def escape_sql(template: Template) -> str:
    parts: list[str] = []
    for item in template:
        if isinstance(item, Interpolation):
            # 如果這是 Template string 中的變量部份，套用一次 sqlescape
            parts.append(sqlescape(str(item.value)))
        else:
            # 如果這是 Template string 中的文字部份，原封不動
            parts.append(item)

id = sqlescape(id)
email = sqlescape(email)
sql = t"SELECT * FROM students WHERE id={id} AND email={email} LIMIT 1";

print(type(sql)) # 不再是一個 str
print(sql) # 輸出顯示這是一個 Template 的 instance
print(escape_sql(sql)) # 可以不用在每條 SQL 字串前，逐個變量處理
