class Product:
    def __init__(self,ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price
        
p1 = Product("D1", "Coke", 3)
p2 = Product("D2", "100plus", 3)
p3 = Product("D3", "A&W", 3)
p4 = Product("D4", "Milo", 2)
p5 = Product("D5", "Chrysanthemum Tea", 2)
p6 = Product("D6", "Mineral Water", 1)

Products = [p1,p2,p3,p4,p5,p6]

def Return_Money(Amount):
    print("Returned Notes:")
    if Amount>50:
        print(f"{Amount//50} RM50")
        Amount=(Amount-(50*(Amount//50)))
    if Amount>20:
        print(f"{Amount//20} RM20")
        Amount=(Amount-(20*(Amount//20)))
    if Amount>10:
        print(f"{Amount//10} RM10")
        Amount=(Amount-(10*(Amount//10)))
    if Amount>5:
        print(f"{Amount//5} RM5")
        Amount=(Amount-(5*(Amount//5)))
    if Amount>=1:
        print(f"{Amount} RM1")


def Listing_Product(Amount):
    print("ID|\tPrice|\tName")
    for x in Products:
        print (x.ID+"|\t  RM"+str(x.price)+"|\t"+x.name)
    print("Remaining = RM"+str(Amount))
    print("Please Insert the Notes (Input Number)")
    print("Please input the ID to select the Drinks")
    print("Enter \"end\" to return the remaining amount")
    user_input=input("input:")
    for x in Products:
        if(user_input.upper()==x.ID):
            if Amount>=x.price:
                print(f"{x.name} is selected")
                Listing_Product(Amount-x.price)
            else:
                print("Not enough Notes, please insert more Notes")
                Listing_Product(Amount)
            break
    else:
        if user_input.isnumeric():
            Listing_Product(Amount + int(user_input))
        elif user_input.upper()=="END":
            Return_Money(Amount);
            print("Thanks for Coming")
        else:
            print("wrong input, please try again")
            Listing_Product(Amount)
    
Listing_Product(0)

import time
time.sleep(100)
