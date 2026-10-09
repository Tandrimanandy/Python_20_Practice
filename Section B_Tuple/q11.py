'''
Question 11: Product Order Details
An e-commerce website stores an order as a tuple containing order ID, product name, quantity, and unit price. 
Write a function to calculate the total order value and display the order details.
'''

def order_details(order):
    order_id, product, quantity, unit_price = order
    total_value = quantity * unit_price

    print(f"Order ID: {order_id} \n Product: {product}  \n  Quantity: {quantity} Unit price: ₹{unit_price:,} \n Total order value: ₹{total_value:}")
order_details(("Ord1234", "Monitor", 3, 799))
print()