# === Ist Product
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

# === IInd Product
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price =  180.50

# === IIIrd Product
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

# === Sales Tax
sales_tax = 0.088

# Customer 1: Initialization
customer_one_total = 0
customer_one_itemization = ""

# Purchase 1
customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

# Purchase 2
customer_one_total += luxurious_lamp_price

customer_one_itemization += "\n" + luxurious_lamp_description

print("Total Pre Tax:")
print(customer_one_total)

# Calculating the tax
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax
print("Total Post Tax:")
print(customer_one_total)

print("Customer One Items:")
print(customer_one_itemization)








