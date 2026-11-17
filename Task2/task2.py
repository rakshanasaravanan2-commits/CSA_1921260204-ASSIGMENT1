from decimal import Decimal

milk_litres = Decimal("10.5")
base_rate = Decimal("30.00")

amount = milk_litres * base_rate

print("Milk Litres:", milk_litres)
print("Base Rate:", base_rate)
print("Total Amount: Rs.", amount)
