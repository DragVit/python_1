#Найдите сумму цифр трехзначного числа.

x = (input("Введите Трехзначиное число: "))
x = str(x)
if len(x) !=3:
    print("Неверное число")
else:
    result = int(x[0]) + int(x[1]) + int(x[2])
    print(result)
