# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

week = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

day = int(input("Выберите номер дня:"))
if day <= 7:
    print ("Выбранный день недели:",week [day-1])
else:
    print ("Нет такого дня")


