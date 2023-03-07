import csv
import datetime



class Pizza:# super class to create a new object
    def __init__(self,name,cost):
        self._cost = cost
        self.name = name
        
    def get_description(self):#Function that defines pizza status, price and ingredients
        return "All of our pizza varieties are thin crust.\nThe pizza you have chosen is {}, price of the pizza is {}$ and its contents are as follows:".format(self.name,self._cost)

    def get_Cost(self):#
        return self._cost


#Classic, Margeherita, Turk_Pizza and The Plain_Pizza classes are the subclass of Pizza class
class Classic(Pizza):

    def __init__(self):
        super().__init__("Classic",120)#Since it is a subclass, it defines the properties of the class in the _init_ function of the super class.

    def get_description(self):#Describe the ingredients
        return super().get_description() + "\nTomato sauce, Mozzarella Cheese, Sausage, Sausage, Olive, Corn, Green Pepper, Thyme."  

    def get_Cost(self):#Showing the cost of the pizza
        return Pizza.get_Cost(self)


#Other classes do the same thing with Classic class
class Margherita(Pizza):
    
    def __init__(self):
        super().__init__("Margherita",110)
            

    def get_description(self):
        return super().get_description() + "\nIt is a Napoli pizza made with Tomatoes, Mozzarella, Basil, Olive Oil and Salt."  

    def get_Cost(self):
        return Pizza.get_Cost(self)


class Turk_Pizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza",115)
            

    def get_description(self):
        return super().get_description() + "\nMushroom, Green Pepper, Sausage, Olive, Bacon, Tomato."   

    def get_Cost(self):
        return Pizza.get_Cost(self)



class Plain_Pizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza",130)
            

    def get_description(self):
        return super().get_description() + "\nCheddar Cheese, Mozzarella, Red Pepper, Tomato, Mushroom, Black Olive, Sausage, Corn Kernels and Thyme"   

    def get_Cost(self):
        return Pizza.get_Cost(self)




#Decorator class is the superclass for the other sauce classes
class Decorator:
    def __init__(self,sauce):
        self.sauce = sauce

    def get_description(self):#Show the sauce
        return "The sauce you have chosen is {}".format(self.sauce)
    
    def get_cost(self):
        return self.cost
            


class Olives(Decorator):
    def __init__(self):
        super().__init__("Olives")

    def get_cost(self):#Shows the sauce price of each class
        return 15
    
    def get_description(self):#Along with superclass, it serves to print the sauce and its price.
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())

#Other sauce classes do the same things
class Mushrooms(Decorator):
    def __init__(self):
        super().__init__("Mushrooms")

    def get_cost(self):
        return 36
    
    def get_description(self):
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())

class Goat_Cheese(Decorator):
    def __init__(self):
        super().__init__("Goat Cheese")

    def get_cost(self):
        return 54
    
    def get_description(self):
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())

class Meat(Decorator):
    def __init__(self):
        super().__init__("Meat")

    def get_cost(self):
        return 48
    
    def get_description(self):
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())
    
class Onions(Decorator):
    def __init__(self):
        super().__init__("Onions")

    def get_cost(self):
        return 12
    
    def get_description(self):
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())

class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn")

    def get_cost(self):
        return 27
    
    def get_description(self):
        return Decorator.get_description(self) + " and the price ise {}$".format(self.get_cost())






#The main function is a function that allows the user to receive data, create objects and perform operations according to the received values.
def main():

    print("Welcome to the POS Pizza\n")

    f = open("Menu.txt", "r",encoding="utf-8")#Reading the Menu.txt file

    print(f.read())#Print the whole menu

    s =""
    while True:
        base = input(("\nPizza Base:"))#It prompts the user for the type of pizza.
        p = Pizza(base,0)
        sauce = input(("Sauce:"))#It prompts the user for the type of sauce.
        s =sauce
        print()

        #It creates objects according to the pizza type and provides information about the pizza and the calculation of its cost.
        if base.lower() == "classic":
            k = Classic()
            print(k.get_description())
            ccost = k.get_Cost()
            p = k
            break

        elif base.lower() == "margherita":
            m = Margherita()
            print(m.get_description()) 
            mcost = m.get_Cost()
            p = m
            break  

        elif base.lower() == "turk pizza":
            t = Turk_Pizza()
            print(t.get_description()) 
            tcost = t.get_Cost()
            p = t
            break

        elif base.lower() == "plain pizza":
            pl = Plain_Pizza()
            print(pl.get_description()) 
            pcost = pl.get_Cost()
            p = pl
            break

        else:
            print("Please choose one of the available pizzas.")
            continue
            
        
    print()
    
    stot = 0

    #By creating objects according to the sauce type, it provides information about the sauce and calculation of its cost
    if s.lower() == "olives":
        ol = Olives()
        print(ol.get_description())
        stot = ol.get_cost()
    elif s.lower() == "mushrooms":
        ms = Mushrooms()
        stot = ms.get_cost()
        print(ms.get_description())
    elif s.lower() == "goat cheese":
        gc = Goat_Cheese()
        stot = gc.get_cost()
        print(gc.get_description())
    elif s.lower() == "meat":
        mt = Meat()
        stot = mt.get_cost()
        print(mt.get_description())
    elif s.lower() == "onions":
        on = Onions()
        stot = on.get_cost()
        print(on.get_description())
    else:
        cr = Corn()
        stot = cr.get_cost()
        print(cr.get_description())
    

   
    total = p.get_Cost() + stot#Sums up the price of pizza and sauce
    print(f"Total fee is {total}$\n")#Shows the total cost

    order = "Pizza type: {}, Sauce: {},".format(p.name,s)
    print()
   
    #It collects information about the customer to save it in the database.
    indentity = input("Identity Number:")
    card_name = input("Name on the card:")
    number = input("Card Number:")
    password = input("Card Password:")


    #Stores the time the order is placed.
    time = datetime.datetime.now()
    timestr = (time.strftime("%x - ""%X"))


    #It creates a csv file and saves the data received from the user in this csv file.
    with open("Orders_Database.csv", "a+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="-")

        csv_writer.writerow([order, indentity, card_name, number, password, timestr])
    



main()