def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        Totaldiscount = discount_percent*price/100
        Final_Price = price- Totaldiscount
        print(Final_Price)
    else:
        Final_Price = price
        print(Final_Price)
    

calculate_discount(1000,21)#example using 1000 as price and 21 as th percent