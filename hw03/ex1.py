# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

list_repeat = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8] # 9, 10 не повторяются
list_dublicate = []
list_repeat_repeat = list_repeat
j = 0
for i in range(len(list_repeat)):
    count_dubl = list_repeat.count(list_repeat[i])
    if count_dubl > 1 and list_repeat[i] not in list_dublicate:
        list_dublicate.append(list_repeat[i])


print(list_repeat)
print(list_dublicate)