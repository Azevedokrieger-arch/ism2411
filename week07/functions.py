#exercise 1 
#define calculate tax function

def calculate_tax(price, rate):
    return price * rate

#calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # $7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # $20.00

#exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # Apply 20% discount
    elif tier == "silver":
        return price * 0.90  # Apply 10% discount
    elif tier == "bronze":
        return price * 0.95  # Apply 5% discount
    else:
        return price

#calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"Discounted price for {tier} tier: ${apply_discount(price, tier):.2f}")

#exercise 3 

# write it out manually first, then reafactor into a function 

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"after gold discount: ${discounted:.2f}")
print(f"after tax: ${after_tax:.2f}")

#refactor into a function 

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#exercise 4 

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

#exercise 6

x = 100  # apple


def double_it():
    global x
    # x = 999  # local another apple (not the same as above)
    return x * 2


print(x)
print(double_it())  # Output: 200
print(x)

#exercise 5 

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    #bug 1: The total was not adding the sales together 
    total += sale
print(f"Total: ${total}")

count = 0
#bug 2: the for loop was missing a colon 
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
#bug 3: the loop was going past the last item in the list 
while i < len(sales):
    print(sales[i])
    i += 1
