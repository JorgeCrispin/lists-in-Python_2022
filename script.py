# Your code below:
toppings = ["pepperoni", "pineapple", "cheese","sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell "+ str(num_pizzas) +" different kinds of pizza!")
#6 create a two dimensional list
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"],[7, "anchovies"], [2, "mushrooms"]]
#print(pizza_and_prices)
print()
print()
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
print(
  
)
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.pop()
#print(pizza_and_prices)
print()
pizza_and_prices.insert(5,[2.5,"peppers"])
pizza_and_prices.sort()
#print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)