# shopping_cart.py

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

#print(products)


#product_ids = []

#while True:
#    product_id = input("Hey please input a product identifier: ")
#    if product_id == "DONE":
#        break
#    else:
#        product_ids.append(product_id)

#print("--------")
#print(product_ids)
#print("--------")

product_ids = [3, 12, 10, 3, 5, 9]

def matching_product(product_identifier):
    products_list = [p for p in products if p ["id"] == product_identifier]
    return products_list[0]

raw_total = 0

for pid in product_ids:
    product = matching_product(int(pid))
    #raw_total = raw_total + product["price"]
    raw_total += product["price"]
    print(str(product["id"]) + " " + product ["name"] + " " + str(product["price"]))

print("----------------------")
print(raw_total)
print("----------------------")

#print Receipt
print("-----------------------")
print("Maria's Grocery Store")
print("------------------------")
print("Web: www.mariasgrocerystore.com")
print("phone: 1.201.344.56777")
#checkout time/date
import datetime

print("Checkout Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))

#shopping cart items formatted as US dollars
print("----------------------")
print("Shopping Cart Items:")
for pid in product_ids:
    product = matching_product(int(pid))
    raw_total += product["price"]
    price_usd = ' (${0:.2f})'.format(product["price"])
    print(" + " + product["name"] + price_usd)
#subtotal+ tax owed
print("----------------------")
print("Subtotal:", '${0:.2f}'.format(raw_total))
Tax = raw_total * 0.08875

print("Plus NYC Sales Tax (8.875%):", '${0:2f}'.format(Tax))
Total = raw_total + Tax
print("Total:", '${0:2f}'.format(raw_total))

#friendly message
print("------------")
print("Thanks for your business! Please come again.")
