import sys

s1 = 'hello'*3;
print(s1)
s2='world'
s1+=s2
print(s1)
s3='abcdefg1234567'
print(s3[::2])

a=5
b=10
print(f'{a}*{b}={a*b}')

list1=[1,3,5,7,100]
list1.append(200)
list1.insert(1,400)
list1+=[1000,2000]
print(list1)

if 3 in list1:
    list1.remove(3)
if 1111 in list1:
    list1.remove(1234)
else:
    list1.append(2345)
print(list1)

list1.pop(len(list1)-1)
print(list1)

list1.clear()
print(len(list1))

list1=['orange','apple','zoo','internationalization','blueberry']
list2=sorted(list1)
print(list2)
list3=sorted(list1,reverse=True)
print(list3)
list4=sorted(list1,key=len)
print(list4)

f=[x for x in range(1,10)]
print(f)
f=[x + y for x in 'abcde' for y in '1234567']
print(f)