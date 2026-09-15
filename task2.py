# todo: Преобразуйте переменную age и foo в число
age='23'
foo='23abc'
age=int(age)
#foo=int(foo) #будет ошибка
print('age как число:',age)
age как число: 23


# Преобразуйте переменную age в Boolean
age='123abc'
age=bool(age)
print('age как boolean',age)
age как boolean True


# Преобразуйте переменную flag в Boolean
flag=1
flag=bool(flag)
print('flag как boolean:',flag)
flag как boolean: True


# Преобразуйте значение в Boolean
str_one='Privet'
str_two=""
one=bool(str_one)
two=bool(str_two)
print('"Privet" как boolean:',one)
"Privet" как boolean: True
print('""как boolean:',two)
""как boolean: False


# Преобразуйте значение 0 и 1 в Boolean
print('как boolean:',bool(0))
как boolean: False
print('как boolean:',bool(1))
как boolean: True


# Преобразуйте False в строку
false=str(False)
print('False как строка:',false)
False как строка: False
print('Тип',type(false))
Тип <class 'str'>
