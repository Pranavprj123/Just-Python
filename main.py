template  = "Dear {name}, take this amount {amount} of bag"

name = "John"
amount = 100

s = template.format(name=name, amount=amount)
print(s)
