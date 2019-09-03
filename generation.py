from dic import dic
import random
a = ''
text = ''

lis = [i for i in list(dic.keys()) if i.endswith('.')]
while a not in dic.keys():
    a = random.choice(lis)
while text.count('.') != 20:
    a = random.choice(dic[a])
    if a in dic.keys():
        text += f'{a} '
print(text)