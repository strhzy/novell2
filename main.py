import random
import time
import json
import csv
from datetime import date
inventory=[]
trail=[]
def save():
    trail_saved = trail
    inv_saved = inventory
    save = {
        "inventory":inv_saved,
        "trail":trail_saved
    }
    with open('save.json','w+') as file:
        json.dump(save,file)
    print("Данные сохранены")
    exit_game()
def load():
    with open('save.json','r')as file:
        save = json.load(file)
    inventory = save['inventory']
    trail = save['trail']
    print("Данные загружены")
    game()
def save_csv():
    trail_saved = trail
    inv_saved = inventory
    save = [
        [date.today(), inv_saved, trail_saved]
    ]
    with open("save.csv",'w+',newline='') as file:
        writer = csv.writer(file)
        for row in save:
            writer.writerow(row)
def exit_game():
    save_csv()
    exit()
def zamok():
    print("Нужно угадать код из 3 цифр")
    print("264 - один номер правильный но не на месте")
    print("189 - один номер правильный и на месте")
    print("152 - два номера правильные и на месте")
    print("894 - нет правильных номеров")
    otv=str(input("Введите ответ: "))
    if otv=="156":
        print("Молодец! Ты нашел сокровище!")
        print("Ваш путь за игру:", trail)
        print("Ваш инвентарь за игру:", inventory)
        exit_game()
    else:
        print("Неправильно! Попробуй еще.")
        zamok()
def zagadka1():
    print("Зимой звезда, весной - вода")
    otvet=str(input())
    if otvet == "Снежинка" or otvet == "снежинка" or otvet == "СНЕЖИНКА":
        print("Молодец! Проходи дальше.")
        game()
    else:
        print("Ладно... Попробуй еще раз")
        zagadka1()
def zagadka2():
    print("Оно принадлежит вам, но остальные используют его чаще вас.")
    otvet = str(input())
    if otvet == "Имя" or otvet == "имя" or otvet == "ИМЯ":
        print("Молодец! Проходи дальше.")
        game()
    else:
        print("Ладно... Попробуй еще раз")
        zagadka2()
def zagadka_hub():
    x = random.randint(1,2)
    match x:
        case 1:
            zagadka1()
        case 2:
            zagadka2()
def death():
    print("Вы сдохли")
    time.sleep(1)
    print("Ваш путь за игру:", trail)
    time.sleep(1)
    print("Ваш инвентарь за игру:", inventory)
    time.sleep(1)
    exit_game()
def octopus():
    trail.append("осьминог")
    print("Вы встретили осьминога в шляпе")
    time.sleep(1)
    print("Осьминог говорит: Добрый день")
    vyboroct = str(input("1. Откуда вы знаете что сейчас день\n2. У вас очень красивая шляпа\n3. У вас отвратительная шляпа"))
    match(vyboroct):
        case "1":
            print("Осьминог говорит: А я и не знаю. Я по привычке говорю. Вы дальше пройти хотите?")
            time.sleep(1)
            print("Ну да")
            time.sleep(1)
            print("Тогда отгадайте загадку")
            zagadka_hub()
        case "2":
            print("Осьминог говорит: Благодарю. Проходите дальше")
            time.sleep(1)
            print("Осьминог пропустил вас дальше и дал пару монет")
            game()
        case "3":
            print("Осьминог говорит: Да как ты посмел?!")
            time.sleep(1)
            print("Осьминог сжал вас шупальцами и задушил")
            death()
        case "s":
            save()
        case _:
            print("Нормально пиши")
            octopus()
def ogr():
    trail.append("огр")
    print("Вы встретили огра\nОгр говорит: Што тибе здесь нада, Кожаный?")
    vyborogr = str(input("1. Я ищу сокровища!\n2. А твое какое дело, Зеленый?\n3. Ничего, я уже ухожу."))
    match vyborogr:
        case "1":
            print("Огр говорит: Тогда тибе нужна крыса-хронитель. Поисчи её где-нибудь сдесь...")
            game()
        case "2":
            print("Огр кричит: ТЫ ШТО АФИГЕЛ?")
            time.sleep(1)
            print("*БОНЬК*")
            time.sleep(1)
            print("Огр ударил вас дубиной")
            time.sleep(1)
            death()
        case "3":
            print("Вы развернулись и ушли до того как огр что-то успел сказать")
            game()
        case "s":
            save()
def nardy():
    print("Это оказались бесконечные нарды")
    time.sleep(1)
    print("Вы до скончания времен играли в нарды")
    time.sleep(1)
    death()
def gnome():
    trail.append("гном")
    print("Вы встретили гнома\nГном очень рад вас видеть\nВидимо он провел здесь много времени")
    time.sleep(1)
    print("Гном говорит: Наконец-то нормальный человек")
    vyborgnome=str(input("1.А что, кроме меня здесь людей нет.\n2.Ты не знаешь где здесь сокровищница?"))
    match vyborgnome:
        case "1":
            print("Как виидишь нет")
            time.sleep(1)
            print("Здесь вообще мало кого встретишь...")
            time.sleep(1)
            print("Ну раз ты здесь давай играть в нарды")
            vyborgnome2=str(input("1.Ладно\n2.Нет спасибо, я пойду"))
            match vyborgnome2:
                case "1":
                    nardy()
                case "2":
                    print("Ну ладно...")
                    time.sleep(1)
                    print("Гном явно расстроился")
                    time.sleep(1)
                    game()
                case "s":
                    save()
        case "2":
            print("И ты про сокровища...")
            time.sleep(1)
            print("Тебе нужно найти крысу которая охраняет сокровища")
            time.sleep(1)
            print("Она загадает тебе загадку, и если решишь то получишь сокоровища")
            time.sleep(1)
            print("Вы поблагодарили гнома и пошли дальше")
            time.sleep(1)
            game()
        case "s":
            save()
def crysa():
    trail.append("крыса")
    print("Вы входите в странную комнату.\nВ комнате очень влажно и сыро.\nВ другом конце сидит небольшая фигура")
    vyborcrys=str(input("1. Подойти к фигуре\n2. Подойти незаметно\n3. Пойти назад"))
    match vyborcrys:
        case "1":
            print("Вы подошли к фигуре и увидели что это крыса.\nКрыса увидела вас и начала говорить.\nКрыса говорит: Здравствуй странник. Я крыса-хранитель.")
            time.sleep(1)
            print("Я охраняю местную сокровищницу. Я так понимаю ты здесь ради неё?")
            time.sleep(1)
            vyborcrys2=str(input("1. Да, я здесь ради сокровищ\n2. Нет, я пришёл чтобы убить тебя\n3. Да не, я по приколу пришел"))
            match vyborcrys2:
                case "1":
                    print("Крыса говорит: Раз ты хочешь сокровища то реши головоломку.")
                    zamok()
                case "2":
                    print("Крыса говорит: Друг, мне проблемы не нужны.")
                    print("Если нужны сокровища, реши головоломку и забирай что хочешь.")
                    zamok()
                case "3":
                    print("Крыса говорит: Ну раз так то держи хотя бы бутылку вина")
                    inventory.append("бутылка вина")
                case "s":
                    save()
        case "s":
            save()

def corridor():
    trail.append("корридор")
    coridor = "Вы наткнулись на перекресток\nЧтобы пойти налево нажмите L\nЧтобы пойти направо нажмите R"
    print(coridor)
    vybor = str(input())
    if  vybor == "L" or vybor == "l" or vybor == "R" or vybor == "r":
        game()
    else:
        print("Неправильный ответ")
        corridor()
def game():
    print("Вы вышли в какую-то комнату комнату")
    x=random.randint(1,41)
    if x>=1 and x<=10:
        corridor()
    if x>=11 and x<=20:
        octopus()
    if x>=21 and x<=30:
        ogr()
    if x>=31 and x<=40:
        gnome()
    if x==41:
        crysa()
print("ИГРА НОВЕЛЛА")
time.sleep(1)
print("Автор идеи - Моя шиза")
time.sleep(1)
text_nach = "Чтобы начать играть, нажмите Y\nЧтобы загрузить сохранение, нажмите L\nЧтобы выйти, нажмите что угодно"
print(text_nach)
nach = str(input())
try:
    if nach == "y" or nach == "Y":
        print("Игра началась")
        game()
    if nach == "Н" or nach == "н":
        print("Переключите раскладку")
        exit()
    if nach=="l" or nach=="L":
        load()
except:
    exit()
