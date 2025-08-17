def calculate_discount(price, discount_percent):
    if (discount_percent) >= 20 :
        return price - (price * (20 / 100))
    else:
        return price
    
print(calculate_discount(float(input("Enter price: ")), float(input("Enter discount percentage: "))))