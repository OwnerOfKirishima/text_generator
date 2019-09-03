text = open("file1.txt", encoding="utf-8").read().split()
dic = {}
for i in range(len(text)-1):
    if text[i] in dic.keys() and text[i+1] not in dic[text[i]]:
        dic[text[i]].append(text[i+1])
    else:
        dic[text[i]] = [text[i+1],] 
open('dic.py', 'w', encoding='utf-8').write(f'dic = {dic}')