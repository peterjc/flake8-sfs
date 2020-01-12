"""Simple example calling str.format(...) directly."""

name = "Peter"
price = 1.2
print(str.format("Hello {}, do you have ${:0.2f}?", name, price))
