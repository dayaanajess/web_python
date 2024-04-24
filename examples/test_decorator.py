#функция декоратор
def decorator(func_parameter):
    #функция обертка
    def wrapper():
        # доп функция №1
        print("before")
        func_parameter()
        # доп функция №2
        print("after")
    return wrapper    

@decorator
#целевая функция
def func_1():
    print("future")

    #вызов функции
func_1()