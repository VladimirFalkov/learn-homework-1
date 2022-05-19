"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
import atexit

def goodbye():
    
    print( "Пока!")





def hello_user(word):
  phrase = input('Как дела? ')
  while phrase != word:
    phrase = input('Как дела? ')
    atexit.register(goodbye)
    break

    
if __name__ == "__main__":
    hello_user("Хорошо")
