'''Варіант 2  1. Написати рекурсивну функцію, що виводить brand авто з найбільшою кількістю
власників.
def getBrand(smth):
#some magic
return brand'''
smth = [{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "owners": {"Bob", "Boba"}
},
    {
        "brand": "Mers",
        "model": "C500",
        "year": 2000,
        "owners": {"Bob"}
    },
    {
        "brand": "Wolkvagen",
        "model": "Polo",
        "year": 2002,
        "owners": {}
    }]


def getBrand(smth):
    '''smth -- список із словників

    Виводить brand авто з найбільшою кількістю власників.

    Якщо список складаэться з одного елементу, то виводиться бренд авто з цього елементу.
    За допомогою lambda-функції значення елементів словників перевіряються за необхідним параметром.
    Функція повертає бренд авто з найбільшою кількістю власників та словник із цим значенням.'''
    if len(smth) == 1:
        return smth[0]["brand"]
    else:
        aA = max(getBrand(smth[:-1]), smth[-1], key=(lambda k: len(k(["owners"]))))
        print(aA["brand"])
        return aA
print(getBrand(smth))

'''2. Написати функцію, що до авто з брендом brand додає нового власника з іменем
name'''
def addOwner(smth,brand, name):
    '''smth -- список із словників
    brand -- бренд авто
    name -- ім'я нового власника

    До словника, який містить певний бренд, додає нового власника.
    Повертає вже змінений словник.'''
    for x in smth:
        if x["brand"]==brand:
            x["owners"].add(name)    # додає ім'я в необхідну множину
    return smth
print(addOwner(smth, "Ford", "Kim"))

'''3. Написати функцію, повертає множину усых власників усіх автомобілів.
def getNames(smth):'''
def getNames(smth):
    '''smth -- список із словників

    Створює множину із усіх власників усіх авто.'''
    aSet_=set()
    for elem in smth:
        aSet_.update(elem["owners"])
    return aSet_
print(getNames(smth))
