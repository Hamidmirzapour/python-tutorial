from ecommerce import shipping

price = 1000000
distance = 100

shipping_cost = shipping.calc_shipping(distance, price)
print(shipping_cost)