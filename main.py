selection_region = int(input('Здравствуйте! Выберите регион проживания: \n 1. Дальний Восток \n 2. Северо-Запад\n 3. Южный округ \n Пропишите нужную цифру: '))

basic_rate = 2
other_rate_region = 10

if selection_region == 1:
    print(f'Вы выбрали Дальний Восток. Ваша ставка составляет {basic_rate}%.')
elif selection_region >= 4 or selection_region <= 0:
    print('Ошибка. Тут явно что-то не так!')

elif selection_region == 2 or 3:
    childs = int(input('\n Продолжим заполнение анкеты. Сколько у Вас детей?\n'))
    card_salary = input('У Вас есть зарплатная карта нашего банка? (Y/N)\n')
    insurance = input('У Вас есть страховка в нашем банке? (Y/N)\n')
    if  childs > 3:
        other_rate_region -= 1
    if card_salary == 'Y':
        other_rate_region -= 0.5
    if insurance == 'Y':
        other_rate_region -= 1.5
    print(f'\nМы готовы одобрить Вам ипотеке под {other_rate_region}%.')

