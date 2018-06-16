# shopping_cart.py
import datetime

products = [{"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)
tax_rate = 0.08875

def sort_key(p):
    return p["department"], p["name"]

def matching_product(product_identifier):
    for p in products:
        if p["id"] == product_identifier:
            return p
    return None

#product_ids = [3, 12, 10, 3, 5, 9]


cart = []
currentDT = datetime.datetime.now()
while True:
    product_id = input("Hey please input a product identifier or DONE: ")
    if product_id == "DONE":
        break
    elif not product_id.isnumeric():
        print("Please, enter a numeric product ID")
    else:
        product = matching_product(int(product_id))
        if product is not None:
            cart.append(product)
        else:
            print("Product id:", product_id, " has not been found")


cart = sorted(cart, key=sort_key)  # sort by deaprtment and product
#print Receipt
print("-----------------------")
print("Maria's Grocery Store")
print("------------------------")
print("Web: www.mariasgrocerystore.com")
print("phone: 1.201.344.56777")
#checkout time/date
#rint("--------")
#print(product_ids)
#print("--------")
raw_total = 0
#cart_items = ""

print("Checkout Time: ", currentDT.strftime("%Y-%m-%d %H:%M:%S"))

#shopping cart items formatted as US dollars
print("----------------------")
print("Shopping Cart Items:")


dept_total = None
dept_name = None
for product in cart:
    if dept_name is None:
        dept_name = product["department"]
        dept_total = 0
        print(dept_name)
    elif dept_name != product["department"]:
        # print previous department Total
        print("{} total: ${:,.2f}".format(dept_name, dept_total))
        dept_name = product["department"]
        dept_total = 0
        print(dept_name)
    raw_total += product["price"]
    dept_total += product["price"]
    print(" + {} ${:,.2f}".format(product["name"], product["price"]))


print("----------------------")
print("Sub total: ${0:,.2f}".format(raw_total))
tax = round(raw_total * tax_rate, 2)
print("Tax: ${0:,.2f}".format(tax))
print("----------------------")
print("Total: ${0:,.2f}".format(raw_total + tax))


#friendly message
print("------------")
print("Thanks for your business! Please come again.")
