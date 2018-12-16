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
def getNames(smth):
    '''smth -- список із словників

    Створює множину із усіх власників усіх авто.'''
    aSet_=set()
    for elem in smth:
        aSet_.update(elem["owners"])    
    return aSet_
print(getNames(smth))
