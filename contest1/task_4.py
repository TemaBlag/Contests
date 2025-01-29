def changer(neg_lst, pos_lst, val):
    """
    Списки neg_lst и pos_lst отсортированные
    Прибавляет значение val к положительному числу, либо отнимает val от отрицательного числа
    """
    neg_len = len(neg_lst)
    pos_len = len(pos_lst)
    if abs(neg_lst[neg_len - 1]) > pos_lst[0]:
        pos_lst[0] += val
        for x in range(1, pos_len):
            if pos_lst[x] < pos_lst[x - 1]:
                pos_lst[x], pos_lst[x - 1] = pos_lst[x - 1], pos_lst[x]
            else:
                break
    else:
        neg_lst[neg_len - 1] -= val
        for x in range(neg_len - 2, 0, -1):
            if neg_lst[x] > neg_lst[x + 1]:
                neg_lst[x], neg_lst[x + 1] = neg_lst[x + 1], neg_lst[x]
            else:
                break
    return


count_checkers, count_corrected_letters, correct_value = [int(x) for x in input().split()]
values = sorted([int(x) for x in input().split()])
board = -1
negative_numbers = []
for el in range(len(values)):
    if values[el] < 0:
        board = el
        negative_numbers.append(values[el])
    else:
        break
positive_numbers = values[board + 1::]
count_positive_numbers = len(positive_numbers)
count_negative_numbers = len(negative_numbers)
if count_negative_numbers % 2:  # нечётное количество отрицательных чисел
    while count_corrected_letters:
        changer(negative_numbers, positive_numbers, correct_value)
        count_corrected_letters -= 1
else:
    if count_negative_numbers:  # чётное количество отрицательных чисел
        count_val_in_pos = round(positive_numbers[0] / correct_value)  # сколько раз придётся прибавить\отнять cor_val,
        count_val_in_neg = round(abs(negative_numbers[count_negative_numbers - 1]) / correct_value)  # изменить знак
        if count_corrected_letters - count_val_in_neg >= 0 and count_corrected_letters - count_val_in_pos >= 0:  # знак
            if count_val_in_neg < count_val_in_pos:  # проще сделать одно положительное число
                new_pos = negative_numbers[count_negative_numbers - 1] + count_val_in_neg * correct_value
                negative_numbers.pop(count_negative_numbers - 1)
                board = 0
                for el in range(count_positive_numbers):
                    if new_pos > positive_numbers[el]:
                        board = el
                    else:
                        break
                positive_numbers.insert(new_pos, board + 1)
            else:
                new_neg = positive_numbers[0] - count_val_in_pos * correct_value
                positive_numbers.pop(0)
                board = count_negative_numbers - 1
                for el in range(count_negative_numbers - 2, 0, -1):
                    if new_neg > negative_numbers[el]:
                        board = el
                    else:
                        break
                negative_numbers.insert(new_neg, board)
            while count_corrected_letters:
                changer(negative_numbers, positive_numbers, correct_value)
                count_corrected_letters -= 1
        else:  # нельзя изменить знак в каком-то случае, либо в двух
            if count_corrected_letters - count_val_in_neg >= 0:
                new_pos = negative_numbers[count_negative_numbers - 1] + count_val_in_neg * correct_value
                negative_numbers.pop(count_negative_numbers - 1)
                board = 0
                for el in range(count_positive_numbers):
                    if new_pos > positive_numbers[el]:
                        board = el
                    else:
                        break
                positive_numbers.insert(new_pos, board + 1)
                while count_corrected_letters:
                    changer(negative_numbers, positive_numbers, correct_value)
                    count_corrected_letters -= 1
            elif count_corrected_letters - count_val_in_pos >= 0:
                new_neg = positive_numbers[0] - count_val_in_pos * correct_value
                positive_numbers.pop(0)
                board = count_negative_numbers - 1
                for el in range(count_negative_numbers - 2, 0, -1):
                    if new_neg > negative_numbers[el]:
                        board = el
                    else:
                        break
                negative_numbers.insert(new_neg, board)
                while count_corrected_letters:
                    changer(negative_numbers, positive_numbers, correct_value)
                    count_corrected_letters -= 1
            else:  # count_val_in_pos и count_val_in_neg < 0
                new_neg = positive_numbers[0] - count_val_in_pos * correct_value
                new_pos = abs(negative_numbers[count_negative_numbers - 1] + count_val_in_neg * correct_value)
                if new_pos < new_neg:
                    positive_numbers[0] = new_neg
                else:
                    negative_numbers[count_negative_numbers - 1] = -1 * new_pos
    else:  # нет отрицательных чисел
        while count_corrected_letters and positive_numbers[0] >= 0:  # получение отрицательного числа из минимального
            positive_numbers[0] -= correct_value  # положительного числа
            count_corrected_letters -= 1
        if positive_numbers[0] < 0:
            negative_numbers.append(positive_numbers[0])  # меняем значение списков положительных чисел и отрицательных
            positive_numbers.pop(0)
            while count_corrected_letters:
                changer(negative_numbers, positive_numbers, correct_value)
                count_corrected_letters -= 1
        # если число осталось неотрицательным, значит count_corrected_letters = 0
print(negative_numbers + positive_numbers)