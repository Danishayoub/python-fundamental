itemcode=int(input("Enter the itemcode:"))
price=int(input("Enter the unit price rs"))
quantity=int(input("Enter the quantity"))
total=quantity*price
discount=total*20/100
netpayable=total-discount
print("=====================================")
print("Item code:",itemcode)
print("=====================================")
print("Unit price in Rs:",price)
print("Quantity taken:",quantity)
print("=====================================")
print("Total amount:",total)
print("Discount amount:",discount)
print("=====================================")
print("Net payable amount:",netpayable)