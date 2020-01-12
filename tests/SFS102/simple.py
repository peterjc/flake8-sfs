"""Example using percent formatting with bytes."""

name = b"Peter"
price = 1.2
message = b"Hello %s, do you have $%0.2f?" % (name, price)
print(message.decode("ascii"))
