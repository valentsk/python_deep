# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things = {"гамак":5, "котелок":2, "спички":1, "палатка":10,  "сухофрукты":1, "ложка":1}
bag = 9
take_this = []
weight = 0
for k, v in things.items():
    if bag - v >= 0:
        take_this.append(k)
        bag -= v
    else:
        continue
print(take_this)