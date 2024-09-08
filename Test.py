#Q1
a = 15
b = 12
print(type(a))
print(type(b))
#Q2
print('a + b =',a+b)
print('a - b =',a-b)
print('a * b =',a*b)
print('a / b =',a/b)
#Q3
c = int(a/b)
print('C is', c)
c = float(a/b)
print('c in float is' ,c)
#Q4
message = 'The result of a divided by b is'
print(message + str(c))
#Q5
if a>b:
    print('True')
else:
    print('False')
if a==b:
    print('True')
elif a!=b:
    print('False')