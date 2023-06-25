# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define SSS = Character('', color="#c8ffc8")
define B = Character('Богдан', color="#c8ffc8")
define D = Character('Детектив', color="#c8ffc8")

#Фон
image bg Black = "Black.jpg"



# Локации
# Комната Допроса
image bg Empty_room_Bogdan_and_TeloSave = "Location/Interrogation_Room/Empty_room_Bogdan_and_TeloSave.png"
image bg Empty_room_Bogdan = "Location/Interrogation_Room/Empty_room_Bogdan.png"
image bg Empty_room = "Location/Interrogation_Room/Empty_room.png"

#Космос
image bg SpaceShip = "Location/Cosmos/StarShip.png"


#Предыстория Богдана
image bg School = "Location/Beginning/School.png"
image bg University = "Location/Beginning/University.png"
image bg Army = "Location/Beginning/Army.png"
image bg Factory = "Location/Beginning/Factory.png"
image bg Factory_Bogdan = "Location/Beginning/Factory_Bogdan.png"






# Персонажи
# Детектив:
image Detective_documents = "Character/Detective/Sits_Image_1.png"
image Detective_card = "Character/Detective/Sits_Image_2.png"
image Detective = "Character/Detective/Sits_Image_3.png"
image Detective_spin = "Character/Detective/Detective_Spin.png"
image Detective_spin_2x = "Character/Detective/Detective_Spin_2x.png"
# Богдан:
image Bogdan_sits_1 = "Character/Bogdan/Bogdan_sits_1.png"
image Bogdan_sits_down_1 = "Character/Bogdan/Bogdan_sits_down_1.png"


#Инициализация
init:
    #Создание собственных позиций на постоянку
    $ left2 = Position(xalign=0.2, yalign=1.0)
    $ right2 = Position(xalign=0.8, yalign=1.1)
    $ Head = Position(xalign=0.5, yalign=2)




# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg SpaceShip
    with fade   #Нужно добавить время что бы задержаться на сцене
    ""
    # Зацикленные звуки часов

    scene bg Empty_room_Bogdan_and_TeloSave
    with fade # Плавный переход с затемнением

    "..."

    # Затихание зацикленного звука часов

    # Звук открывающийся двери

    show Detective_spin_2x at Head # Добавить плавное появление персонажа
    with dissolve

    D "Оставьте нас"

    show bg Empty_room_Bogdan with dissolve
    "Телохранители покинули комнату"

    hide Detective_spin_2x with dissolve

    # Звуки: подвинули стул и сел

    scene bg Empty_room
    with fade

    show Detective_documents with dissolve:
        xalign 0.8 yalign 1.3

    show Bogdan_sits_down_1 with dissolve:
        xalign 0.2 yalign 1.3

    D "Илларион Богдан Игоревич. Родился в 2004 году на планете Земля"

    hide Bogdan_sits_down_1
    hide Detective_documents

    show bg School with dissolve

    D "Начальное образование получили в муниципально бюджетном образовательном учреждение"

    show bg University with dissolve

    D "Отучившись 11 классов поступили в институт"

    show bg Army with dissolve

    D "Поступили на военную кафедру"

    show bg Factory_Bogdan with dissolve

    D "И какое то время работа на заводе по производству беспилотников"

    scene bg Empty_room
    with fade

    show Bogdan_sits_down_1 with dissolve:
        xalign 0.2 yalign 1.3

    show Detective_documents with dissolve:
        xalign 0.8 yalign 1.3

    D "Всё верно?"

    B "Да"

    D "Отлично, а теперь перейдём к самому интересному..."

    scene bg Black
    with fade

    "Спасибо за прохождение Альфы"

    return