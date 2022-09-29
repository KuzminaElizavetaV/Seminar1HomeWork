''' задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
 первое число, второе число и операцию, после чего применяет операцию к введённым числам
 ("первое число" "операция" "второе число") и выводит результат на экран.
 Поддерживаемые операции: +, -, /, *, mod, pow, div, где
 mod — это взятие остатка от деления,
 pow — возведение в степень,
 div — целочисленное деление.

 Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
 Обратите внимание, что на вход программе приходят вещественные числа.

 Sample Input 1:
 5.0
 0.0
 mod
 Sample Output 1:
 Деление на 0!

 Sample Input 2:
 -12.0
 -8.0
 *
 Sample Output 2:
 96.0

 Sample Input 3:
 5.0
 10.0
 /
Sample Output 3:
0.5 '''
num_1 = float(input('Введите первое число:  '))
num_2 = float(input('Введите втрое число:  '))
operation = input('Введите операцию: +, -, /, *, mod, pow, div, где mod — это взятие остатка от деления, pow — возведение в степень, div — целочисленное деление:  ')
result = 0
if operation == '+':
    result = num_1 + num_2
elif operation == '-':
    result = num_1 - num_2
elif operation == '/' and num_2 > 0:
    result = num_1 / num_2
elif operation == '/' and num_2 == 0:
    print('Делить на 0 нельзя!!!')
elif operation == '*':
    result = num_1 * num_2
elif operation == 'mod' and num_2 > 0:
    result = num_1 % num_2
elif operation == 'mod' and num_2 == 0:
    print('Делить на 0 нельзя!!!')
elif operation == 'pow':
    result = num_1 ** num_2
elif operation == 'div' and num_2 > 0:
    result = num_1 // num_2
elif operation == 'div' and num_2 == 0:
    print('Делить на 0 нельзя!!!')
else:
    print('Этот калькулятор не поддерживает эту операцию!')
print(result)