import requests

# x=3
# if x==2 :
#     print(2)
# else:
#     print(3)



def getProduct(id):
    req=requests.get('https://fakestoreapi.com/products/'+str(id))
    return req.json()

def deleteProduct(id):
    req= requests.delete('https://fakestoreapi.com/products/'+str(id))
    if req.status_code==200:
        print("success")
        return True
    else: 
        print(req.status_code)
        return False

def getAllProducts():
    req=requests.get('https://fakestoreapi.com/products/')
    for p in req:
        print(p)
        #return req.json()

def countingType():
    req= requests.get('https://fakestoreapi.com/products/categories')
    if (req.count>0):
        print(req)
    else:
        print("There is no any categories")
    
product=getProduct(3)
print(product)
print(getAllProducts())
print(countingType())
# req= requests.get('https://fakestoreapi.com/products/5')
# print(req.text)
# print(req.json())
