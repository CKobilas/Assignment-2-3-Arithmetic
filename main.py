# Furniture.py - This program calculates profits and sales prices for a furniture company.


ItemName = "TV Stand"
RetailPrice = 325.00
WholesalePrice = 200.00

Profit = RetailPrice - WholesalePrice
SalePrice = RetailPrice - (RetailPrice * 0.25)
SaleProfit = SalePrice - WholesalePrice

print("Item Name: " + ItemName)
print("Retail Price: $" + str(RetailPrice))
print("Wholesale Price: $" + str(WholesalePrice))
print("Profit: $" + str(Profit))
print("Sale Price: $" + str(SalePrice))
print("Sale Profit: $" + str(SaleProfit))