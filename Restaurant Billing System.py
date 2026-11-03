print("..Welcome to the Restaurant Billing System!..")


customer_name = input("Enter customer name: ")
print("Customer_name:", customer_name)
item1 = input("Enter item 1: ")
print("Item1:", item1)
item2 = input("Enter item 2: ")
print("Item2:", item2)
item3 = input("Enter item 3: ")
print("Item3:", item3)
item4 = input("Enter item 4: ")
print("Item4:", item4)
item5 = input("Enter item 5: ")
print("Item5:", item5)
item1_price = float(input("Enter item 1 price: "))
print("Item1_price:", item1_price)
item2_price = float(input("Enter item 2 price: "))
print("Item2_price:", item2_price)
item3_price = float(input("Enter item 3 price: "))
print("Item3_price:", item3_price)
item4_price = float(input("Enter item 4 price: "))
print("Item4_price:", item4_price)
item5_price = float(input("Enter item 5 price: "))
print("Item5_price:", item5_price)
total_price = item1_price + item2_price + item3_price + item4_price + item5_price
print("Total_price:", total_price)

discount = 0.0
if total_price >= 1000:
  discount = 0.15
  discount_reason = "Total Price Discount (15%)"
elif total_price >= 500:
  discount = 0.1
  discount_reason = "Total Price Discount (10%)"
elif total_price >= 300:
  discount = 0.05
  discount_reason = "Total Price Discount (5%)"
else:
  discount = 0.0
  discount_reason = "No Discount"

discount_amount = total_price * discount
final_price = total_price - discount_amount

#Receipt
print("\n" + "="*40)
print("             BILL RECEIPT")
print("="*40)
print(f"Customer Name: {customer_name}")
print(f"Item 1: {item1} - ${item1_price:.2f}")
print(f"Item 2: {item2} - ${item2_price:.2f}")
print(f"Item 3: {item3} - ${item3_price:.2f}")
print(f"Item 4: {item4} - ${item4_price:.2f}")
print(f"Item 5: {item5} - ${item5_price:.2f}")
print("-"*40)
print(f"Total Price: r{total_price:.2f}")
print(f"Applied Discount: {discount_reason}")
print(f"Discount Amount: -r{discount_amount:.2f}")
print("-"*40)
print(f"Final Price: r{final_price:.2f}")
print("="*40)
print("Thank you for shopping with us!")
