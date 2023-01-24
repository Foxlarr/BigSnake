# Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def jokes(n: int, repeat: bool = False):

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    Jcount = []
    list_min = min(no, adv, adj)

    for i in range(len(list_min) % n if repeat else n):
        num = randrange(len(list_min))
        Jcount.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}" if repeat
                         else f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return Jcount


print(jokes(100, True))
