"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('Введите ваш возраст ' ))


def main():

   # Эта функция вызывается автоматически при запуске скрипта в консоли
    #В ней надо заменить pass на ваш код

    if age <= 7:
        ans = "Вы должны учиться в детском саду"
    elif 7 < age <= 17:
        ans = 'Вы должны учиться в школе!'
    elif 17 <age < 21:
        ans='Вы должны учиться в ВУЗе!'
    else:
        ans='Вы должны работать!'
    print(ans)
    


if __name__ == "__main__":
    main()
