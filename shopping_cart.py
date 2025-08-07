#shopping cart

foods = []
prices = []
total = 0      #we want it to have multiple values thats why we make it a zero

while True:     #is used to create an infinite loop
    food = input("Enter the food item or press q to quit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-----YOUR CART-----")

for food in foods:
    print(food, end =" ")
    
for price in prices:
    total += price

print("\n")
print(f"Your total is R{total}")

print("Thank you for shopping with us :)")

        
        

    