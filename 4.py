Number_of_years=input('Введите количество лет')
Number_of_exhibits=input('Введите количество экспонатов')
#60*8=480(столько минут будет проводить человек в музее за день), 480/5=96(столько экспонатов посмотрит человек за день)
Viewed_exhibits=((((int(Number_of_years))//4)*366)+(((int(Number_of_years))-((int(Number_of_years))//4))*365))*96
print("Просмотренно",int(Viewed_exhibits),"экспонатов")
#для того чтобы определить количество вискосных годов разделим введеное колисество годов на 4
#целое число после деление и есть количество високосных годов
#в случае если полученное число имеет дробную часть,её можно просто отбросить)
#умножим полученное количество високосных годов на 366, найдем количество обычных годов и умножим на 365
#сложим полученные значения и умножим на 96(количество посмотренных экспонатов за день)
#первый пункт задания выполнен
Years_spend=(((int(Number_of_exhibits))/96)/365)
print("Потрачено","{:7.1f}".format(Years_spend),"лет")
#Введённое количество экспонатов разделим на 96 (количество просмотенных экспонатов за день)
#Мы получили количество дней потраченных на просмотр введённого количества экспонатов
#Далее разделим количество найденных дней на 365(количество дней в году)
#Мы получили количество лет потраченных на просмотри введённого числа экспонатов




