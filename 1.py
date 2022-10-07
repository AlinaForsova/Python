Name=input('Введите имя студента')
Surname=input('Введите фамилию студента')
Year_of_birth=input('Введите год рождения студента')
print(Name+'_'+Surname +'_'+Year_of_birth)
Replacement_surname=Name
Name=Surname
Surname=Replacement_surname
Year_of_birth=int(Year_of_birth)+60
print(Name,Surname,Year_of_birth)

