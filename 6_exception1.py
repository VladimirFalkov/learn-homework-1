"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def hello_user(word):
  phrase = input('Как дела? ')
  while phrase != word:
    phrase = input('Как дела? ')
    

    
if __name__ == "__main__":
    try:   
        hello_user("Хорошо")
    except KeyboardInterrupt:
        print()
        print("Пока!")
   