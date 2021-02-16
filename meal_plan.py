import random
from collections import Counter

class meal:
    def __init__(self, name, ingrd1=None, ingrd2=None, ingrd3=None, ingrd4=None, ingrd5=None, ingrd6=None, ingrd7=None, ingrd8=None):

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

class aisle:
    def __init__(self, aisle_Title, aisle_Num, ingrd1=None, ingrd2=None, ingrd3=None, ingrd4=None, ingrd5=None, ingrd6=None, ingrd7=None, ingrd8=None, ingrd9=None, ingrd10=None, ingrd11=None, ingrd12=None, ingrd13=None, ingrd14=None, ingrd15=None, ingrd16=None):

      #Assgn var values
        self.aisle_Title = aisle_Title
        self.aisle_Num = aisle_Num
        self.ingrd1 = ingrd1
        self.ingrd2 = ingrd2
        self.ingrd3 = ingrd3
        self.ingrd4 = ingrd4
        self.ingrd5 = ingrd5
        self.ingrd6 = ingrd6
        self.ingrd7 = ingrd7
        self.ingrd8 = ingrd8
        self.ingrd8 = ingrd8
        self.ingrd9 = ingrd9
        self.ingrd10 = ingrd10
        self.ingrd11 = ingrd11
        self.ingrd12 = ingrd12
        self.ingrd13 = ingrd13
        self.ingrd14 = ingrd14
        self.ingrd15 = ingrd15
        self.ingrd16 = ingrd16

    def ingrd_array(aisle):
        ingrd_ary = [ aisle.ingrd1, aisle.ingrd2, aisle.ingrd3, aisle.ingrd4, aisle.ingrd5, aisle.ingrd6, aisle.ingrd7, aisle.ingrd8, aisle.ingrd9, aisle.ingrd10, aisle.ingrd11, aisle.ingrd12, aisle.ingrd13, aisle.ingrd14, aisle.ingrd15, aisle.ingrd16 ]
        return  ingrd_ary

#####data######
m1 = meal("Lasanga", "Tomato Sauce", "Tomato Paste", "Garlic", "Oregano", "Milk/Cream", "Pepper", "Salt", "Spice")
m2 = meal("Halumi Sanwhiches","Halummi", "Basil","Garlic", "Oregano", "Spinach", "Pepper", "Salt", "Spice")
m3 = meal("Shrimp Scampi","Shrimp", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m4 = meal("Quiche","Eggs", "Cheese", "Garlic", "Leeks", "Olive Oil", "Pepper", "Salt", "Spice")
m5 = meal("Fish","COD or Salmon", "Ginger","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m6 = meal("Veggie Shepard’s pi","Shrimp", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m7 = meal("Pizza (homemade)", "Pizza Dough", "Tomato Sauce","Garlic", "Basil", "Olive Oil", "Pepper", "Salt", "Pineapple")
m8 = meal("Thai curry","Curry Suace", "Butter","Garlic", "Lemon", "Chicken Breast", "Peppers", "Salt", "Spice")
m9 = meal("Butter Sauce - Paneer", "Chicken Breast", "Butter Suace", "Garlic", "Rice", "Naan", "Pepper", "Salt", "Spice")
m10 = meal("Pad Thai","Rice Noodles", "Ginger","Garlic", "Lime", "Chicken Breast", "Pepper", "Salt", "Spice")
m11 = meal("Leek and Potato Soup","Leeks", "Potatos","Garlic", "Boulon Cubes-No Salt", "Carrots", "Pepper", "Salt", "Spice")
m12 = meal("Tomato soup / grilled cheese","Sour Dough Bread", "Butter","Garlic", "Cheese", "Basil", "Pepper", "Salt", "Tomato Sauce")
m13 = meal("Stir fry", "Assorted Veggies", "Avo Oil","Garlic", "Lemon", "Ginger", "Pepper", "Salt", "Spice")
m14 = meal("Bruschetta - Sandwich","Tomatos", "Mozzarella","Garlic", "Pesto", "Olive Oil", "Pepper", "Salt", "Buns")
m15 = meal("Falafel","ChickPeas", "Butter","Garlic", "Lemon", "Edmame", "Pepper", "Salt", "Spice")
m16 = meal("Chicken and yam","Chicken Breast", "Yams", "Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m17 = meal("Greek spanakopita and potato", "Philo (Frozen)", "Butter","Garlic", "Lemon", "Olive Oil", "Pepper", "Salt", "Spice")
m18 = meal("Bhan Mi", "Tofu", "Buns","Garlic", "Carrots", "Dikon", "Pepper", "Salt", "Spice")
m19 = meal("Tacos", "Chicken Breast", "Tort Wraps","Garlic", "Yams", "Colslaw", "Pepper", "Salt", "Spice")

#(is this more for total shopping list)
a1 = aisle("Baby_Bathroom", 1, "Toliet_Paper", "Denture Tabs", "Tooth Paste" )
a2 = aisle("Health Food", 2, "Tortila Chips", "Salsa", "Pasta(spelt)", "Boulon Cubes-No Salt")
a3 = aisle("Fruits and Veggies",3, "Assorted Veggies", "Tomatos", "Carrots", "Mushroom", "Ginger", "Leeks", "Peppers", "Agrugla", "Spinach", "Garlic", "Lime",  "Lemon",  "Basil", "Potatos", "Dikon", "Yams")
a4 = aisle("Cleaning", 4, "Dish Packets", "Detergent")
a5 = aisle("Baking", 5, "Unbleach All_P Flour", "Baking Soda")
a6 = aisle("Deli", 6,"Chicken Breast", "Shrimp",  "COD or Salmon", "Hummus", "Cheese", "Mozzarella", "Ricatta", "Feta", "Tofu", "Pesto", "Halummi")
a7 = aisle("Snacks_and_Canned", 7, "Potato_Chips", "Tomato Sauce", "Tomato Paste", "Pineapple", "ChickPeas")
a8 = aisle("World Foods", 8, "Rice Noodles", "Butter Suace", "Curry Suace", "Avo Oil", "Olive Oil", "Rice",  "Spice", "Pepper", "Salt", "Oregano")
a9 = aisle("Dairy", 9, "Butter", "Yoghurt", "Milk/Cream", "Sour Cream", "Eggs")
a10 = aisle("Frozen", 10,"Pizza Dough", "Pie Crusts", "Philo (Frozen)", "Edmame" )
a11 = aisle("Bakery", 11, "Naan", "Tortila Big", "Tortila Small", "Sour Dough Bread", "Buns")

#####data######

#Load Arrays
meals = [m1, m2, m3, m4, m5, m6, m7, m8, m9 , m10, m11, m12, m13, m14, m15, m16, m17, m18]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
aisles = [a1, a2, a3, a4, a5, a6, a7, a8, a9 , a10, a11]

#search aisle function
def search_aisle(ingredient):
    for aisle in aisles:
        # print (aisle.aisle_Title)
        if ingredient in aisle.ingrd_array():
            return aisle.aisle_Num, aisle.aisle_Title
            break

#Print Each day and unqiue selection for each day
def meal_per_day(days): #
    meallist = []
    for day in days:
        mealselected = random.choice(meals)
        #Loop to handle conflict and retry
        while True:
            #decided if selected meal is in the array
            if mealselected not in meallist:
                meallist.append(mealselected)
                print ("\n" + day + ": "+ mealselected.name)
                mealselected.ingrd_list()
                print ("+++++++")
                break
            else:
                mealselected = random.choice(meals)

    return meallist

# groceries list
def grocery_list_map(mealsselected):
    #define list to become of all ingriendts
    ingdrs_tuple = ()
    ingrd_list_tuple = []

    #loop over all meals
    for meal in mealsselected:
        #loop over all ingredients for each meal
        for i in meal.ingrd_array():
            # Call search aisle Function returns None if not found
            aisle_info = search_aisle(i)

            if aisle_info == None:
                print(i + " Ingredient Not Found In Aisle - Please Update Aisle Object")
            else:

                #Create ingredient from meal and Aisle info tuple
                ingdrs_tuple = (i, aisle_info[0], aisle_info[1])

                #add to list of tuples
                ingrd_list_tuple.append(ingdrs_tuple)

    # count and then sort the counted list
    counted_tuple_list = Counter(ingdrs_tuple for ingdrs_tuple in ingrd_list_tuple)
    # Not accessing the actual counted value yet, but it does remove the duplicates
    # as counter returns a dict of ()(tu,p,le): # )
    sorted_tuple_list = sorted(counted_tuple_list, key=lambda ingdrs_tuple: ingdrs_tuple[1])

    print ("\n - Grocery List - ")
    #print it left justified
    for key, value, aisle_num in sorted_tuple_list:
        print (f'')
        print (f'Item: {key:<15}')
        print (f'Aisle: {aisle_num:<20}{value}')

#Print all grocery based on the meals selected for the week.
grocery_list_map(meal_per_day(days))
