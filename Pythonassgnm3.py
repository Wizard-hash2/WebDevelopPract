def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        Totaldiscount = discount_percent*price/100
        Final_Price = price- Totaldiscount
        return Final_Price
    else:
        Final_Price = price
        return Final_Price
    

print(calculate_discount(1000,19))