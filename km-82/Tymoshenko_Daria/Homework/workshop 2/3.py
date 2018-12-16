smth=[{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "owners":{"Bob","Boba"}
},
{
  "brand": "Mers",
  "model": "C500",
  "year": 2000,
  "owners":{"Bob"}
},
{
  "brand": "Wolkvagen",
  "model": "Polo",
  "year": 2002,
  "owners":{}
}]
def getBrand(smth):
    '''smth -- список із словників

    Виводить brand авто з найбільшою кількістю власників.
    
    Якщо список складаэться з одного елементу, то виводиться бренд авто з цього елементу.
    За допомогою lambda-функції значення елементів словників перевіряються за необхідним параметром.
    Функція повертає бренд авто з найбільшою кількістю власників та словник із цим значенням.'''
    if  len(smth)==1:
        return smth[0]["brand"]
    else:
        aA=max(getBrand(smth[:-1]), smth[-1], key=(lambda k: len(k(["owners"]))))
        print(aA["brand"])
        return aA
print(getBrand(smth))
 
