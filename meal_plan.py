import random
from collections import Counter
# Functionality to add:
# Email me the list every Sunday
# turn ingredients into an tuples (ingrd name + quantity)
# move the data/objects to a file in json format and read it in.
# put it in a webserver(this implies database)

class meal:
    def __init__(self, name, ingrd1, ingrd2, ingrd3, ingrd4, ingrd5, ingrd6, ingrd7, ingrd8):

      #Assgn var values
        self.name = name
        self.ingrd1 = ingrd1
        self.ingrd2 = ingrd2
        self.ingrd3 = ingrd3
        self.ingrd4 = ingrd4
        self.ingrd5 = ingrd5
        self.ingrd6 = ingrd6
        self.ingrd7 = ingrd7
        self.ingrd8 = ingrd8

    def ingrd_list(meal):
        print ( "Ingredients: "+ meal.ingrd1 +", "+ meal.ingrd2 +", "+ meal.ingrd3 +", "+ meal.ingrd4 +", "+ meal.ingrd5 +", "+ meal.ingrd6 +", "+ meal.ingrd7 +", "+ meal.ingrd8 + "\n")

    def ingrd_array(meal):
        ingrd_ary = [ meal.ingrd1, meal.ingrd2, meal.ingrd3, meal.ingrd4, meal.ingrd5, meal.ingrd6, meal.ingrd7, meal.ingrd8 ]
        return  ingrd_ary

#####data######
m1 = meal("Lasanga","Tomato Suace", "Tomato Paste","Garlic", "Oregino", "Milk/Cream", "Pepper", "Salt", "Spice")
m2 = meal("Halumi Sanwhiches","Halummi", "Basil","Garlic", "Oregino", "Spinach", "Pepper", "Salt", "Spice")
m3 = meal("Shrimp Scampi","Shrimp", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m4 = meal("Quiche","Eggs", "Cheddar Cheese", "Garlic", "Leeks", "Olive Oil", "Pepper", "Salt", "Spice")
m5 = meal("Fish","COD or Salmon", "Ginger","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m6 = meal("Veggie Shepard’s pi","Shrimp", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m7 = meal("Pizza (homemade)" ,"Pizza Dough", "Tomato Sauce","Garlic", "Basil", "Olive Oil", "Pepper", "Salt", "Pineapple")
m8 = meal("Thai curry","Curry Suace", "Butter","Garlic", "Lemon", "Chicken Breat", "Peppers", "Salt", "Spice")
m9 = meal("Butter Sauce - Paneer", "Chicken Breast", "Butter Suace", "Garlic", "Rice", "PlaceHolder", "Pepper", "Salt", "Spice")
m10 = meal("Pad Thai","Rice Noodles", "Ginger","Garlic", "Lime", "Chicken Breast", "Pepper", "Salt", "Spice")
m11 = meal("Leek and Potato Soup","Leeks", "Potatos","Garlic", "Buolon Cubes", "Carrots", "Pepper", "Salt", "Spice")
m12 = meal("Tomato soup / grilled cheese","Sour Dough Bread", "Butter","Garlic", "Cheese", "Basil", "Pepper", "Salt", "Tomato Sauce")
m13 = meal("Stir fry", "Assorted Veggies", "Avo Oil","Garlic", "Lemon", "Ginger", "Pepper", "Salt", "Spice")
m14 = meal("Bruschetta - Sandwich","Tomatos", "Mozzarella","Garlic", "Pesto", "Olive Oil", "Pepper", "Salt", "Bun")
m15 = meal("Falafel","ChickPeas", "Butter","Garlic", "Lemon", "Edmame", "Pepper", "Salt", "Spice")
m16 = meal("Chicken and yam","Chicken Breast", "Yams", "Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m17 = meal("Greek spanakopita and potato", "Philo (Frozen)", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m18 = meal("Bhan Mi", "Tofu", "Buns","Garlic", "Carrots", "Dikon", "Pepper", "Salt", "Spice")
m19 = meal("Tacos", "Chicken Breat", "Tort Wraps","Garlic", "Yams", "Colslaw", "Pepper", "Salt", "Spice")
#####data######

#Load Arrays
meals = [m1, m2, m3, m4, m5, m6, m7, m8, m9 , m10, m11, m12, m13, m14, m15, m16, m17, m18]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Print Each day and unqiue selection for each day
def meal_per_day(days): #
    meallist = []
    for day in days:
        mealselected = random.choice(meals)
        #Loop to handle conflict and retry
        stoploop = 1
        while stoploop == 1:
            #decided if selected meal is in the array
            if mealselected not in meallist:
                meallist.append(mealselected)
                print ("\n" + day + ": "+ mealselected.name)
                mealselected.ingrd_list()
                print ("+++++++")
                stoploop = 0
            else:
                mealselected = random.choice(meals)
                stoploop = 1

    return meallist

# groceries list
def grocery_list(mealsselected):
    #define list to become of all ingriendts
    ingdrs = []
    #loop over all meals
    for meal in mealsselected:
        #loop over all ingredients for each meal
        for i in meal.ingrd_array():
            #add ingredients one by one to 1 list
            ingdrs.append(i)
        #convert to dict ingredients and count
        ingdrs_dict = dict(Counter(ingdrs))
    print ("\nGrocery List: ")
    #print it left justified
    for key, value in ingdrs_dict.items():
        print (f'{key:20}{value}')

grocery_list(meal_per_day(days))
