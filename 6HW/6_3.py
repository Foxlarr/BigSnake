# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def magic(t):
    names_dict = {}
    for i in sorted(t):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict



print(magic("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))





















# d['id'] = list(a[0])[0] 
#     # (хрень берет элемент листа,делает из элемента лист, дергает из него 1вую букву)