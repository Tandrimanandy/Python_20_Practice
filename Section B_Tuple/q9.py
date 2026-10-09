'''
Question 9: Mobile Product Details
An electronics store stores mobile details in a tuple containing
brand, model, price, and storage capacity. Write a function to
display the details and check whether the mobile price is below
₹30,000.

'''

def mobile_details(mobile):
    brand, model, price, storage = mobile

    print(f"Brand: {brand} \n Model: {model} \n Price: ₹{price:,} \n Storage: {storage} GB \n Price below ₹30,000:  {price} < 30000")
mobile_details(("Samsung", "Galaxy A51", 20000, 128))
print()
