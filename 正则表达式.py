import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('www.runoob.com', 'www.runoob.com'))         # 不在起始位置匹配

print(re.match('html', '<html>www.runoob.com</html>'))         # 不在起始位置匹配
