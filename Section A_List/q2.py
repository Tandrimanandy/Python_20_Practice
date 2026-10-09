'''
Question 2: Online Mobile Store
An online store maintains a list of mobile prices. Write a function to display all mobiles costing more than ₹20,000, 
calculate the total inventory value, and find the most expensive mobile price.
'''

def mob_store(prices):
    expensive = [price for price in prices if price > 20000]
    total_value = sum(prices)

    print(f"Mobiles costing more than ₹20,000: {expensive} \n Total inventory value: ₹ {total_value:,} \n Most expensive mobile: ₹{max(prices):,}")
   

mob_store([12111, 26000, 18524, 45000, 31000, 9990])
print()