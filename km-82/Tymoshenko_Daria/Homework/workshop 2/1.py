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
