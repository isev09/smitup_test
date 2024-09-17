# Для решения файла А мы будем использовать переборный алгоритм
# Данный алгоритм проще изучить и написать, однако с его помощью не получится решить файл B
# Если стоит задача решить оба файла, советую сразу писать использовать второй вариант решения

f = open("27_A.txt")        # Откроем файл с исходными данными
n = int(f.readline())       # Прочитаем первую строчку (количество чисел)
nums = [int(s) for s in f]     # Создадим список и запишем в него все числа

max_summ, len_max_summ = 0, 999999

# Перебираем все возможные последовательности
# i указывает на первое, а j на последнее число последовательности
for i in range(n):
    for j in range(i, n):
        # Подсчитаем сумму как сумму всех элементов среза
        summ = sum(nums[i:j+1])
        # Проверяем удовлетворяет ли сумма условию
        if summ % 89 == 0:
            # Если подходящая сумма превышает предыдущий максимум, то
            # обновим максимум и запишем длину последовательности
            if summ > max_summ:
                max_summ = summ
                len_max_summ = len(nums[i:j+1])
            # Если текущая сумма и максимальная совпадают, то
            # запишем минимальную из длин этих последовательностей
            if summ == max_summ:
                len_max_summ = min(len_max_summ, len(nums[i:j+1]))

# По итогу в len_max_summ будет лежать длина той последовательности,
# которая имеет максимальную сумму и минимальную длину
print(len_max_summ)