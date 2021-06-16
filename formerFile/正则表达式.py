import re

string = """
<a href='www.runoob.com'>first</a>,
<a href='www.baidu.com'>second</a>
"""

r = re.findall(r'<a href=\'([www].*)\'>(.*)</a>', string)
print(r)
