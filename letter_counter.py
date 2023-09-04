# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# Статья находится в документе wiki.txt

f = open("wiki.txt", "r")

lst = list(f)
text_raw = []

for i in lst:
    str(i).strip(",.")
    text_raw += (str(i).split())

for i in range(len(lst)):
    d = {x: text_raw.count(x) for x in text_raw}

for k,v in d.items():
    if v > 10:
        print(f"{k}: {v}")
