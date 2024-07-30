def calc_shipping(distance, price):
    if distance > 500:
        if price > 100000:
            return price * 0.1
        else:
            return price * 0.05
    else:
        if price > 100000:
            return price * 0.08
        else:
            return price * 0.03