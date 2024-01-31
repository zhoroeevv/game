
#  ИГРА ПОХОД В ТОРГОВЫЙ ЦЕНТР "ГЛОБУС"

import random


def зарегистрироваться():
    cod = random.randint(1000, 9999)
    print(f"Ваш одноразовый код: {cod}")
    print("Пожалуйста, сохраните его.")
    return cod

def поход_в_Глобус():
    print("добро пожаловать в Глобус")
    print("По пути вас остановливает охранник.")

    ответ = input("Охранник: Здравствуйте! можно посмотрет ваши сумки? (да/нет): ").lower()

    if ответ == "да":
        examination = input("Охранник: Пройдете через металлодетектор? (да/нет): ").lower()

        if examination == "да":
            print("Охранник: Отлично! Просто проходите. Приятных вам покупок!")
        else:
            регистрация = input("Охранник: если не хотите пройти металодетектор тогда  вы должны зарегистрироваться и получить одноразовый код? (да/нет): ").lower()

            if регистрация == "да":
                одноразовый_код = зарегистрироваться()
                код = int(input("Охранник: Пожалуйста, введите ваш одноразовый код: "))

                if код == одноразовый_код:
                    print("Охранник: Спасибо за регистрацию. Проходите, приятных вам покупок!")
                else:
                    print("Охранник: К сожалению, введенный код не совпадает. Доступ запрещен.")
            else:
                print("Охранник: Извините, но мы не можем вас пропустить без регистрации.")
    elif ответ == "нет":
        print("проход запрешен")
    else:
        print("Охранник: Извините, я вас не понял. Пожалуйста, ответьте 'да' или 'нет'.")

if __name__ == "__main__":
    поход_в_Глобус()


