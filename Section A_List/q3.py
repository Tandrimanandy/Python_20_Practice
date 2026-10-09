""" 
Question 3: Shopping Cart Management
A customer adds products to a shopping cart. Write a function that accepts a list of product names and performs the following operations:
Add a new product.
Remove a purchased or unwanted product.
Display the final cart.
Count the total number of products.
"""




def manage_cart(cart, add_item=None, remove_item=None):
    if add_item:
        cart.append(add_item)
        print(f"Added: {add_item}")

    if remove_item:
        if remove_item in cart:
            cart.remove(remove_item)
            print(f"Removed: {remove_item}")
        else:
            print(f"{remove_item} is not in the cart.")

    print("Final cart:", cart)
    print(f"Total products: {len(cart)}")
    return cart

cart = ["Apple", "Laptop", "HDphone", "Jukini", "Orange","Pen", "Mamabari"]
manage_cart(cart, add_item=input(f"Enter the item :"), remove_item="Shirt")
print()
