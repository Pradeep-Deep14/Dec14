def calculate_price(*,price, quantity, discount=None):
    if discount is None:
        total_price = price * quantity
    else:
        discount_amount =(price * quantity * discount) /100
        total_price = price * quantity - discount_amount
        return total_price
print(calculate_price(price=100, quantity=20, discount=30))


#*, takes only keyword arguments