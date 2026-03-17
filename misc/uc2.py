inputs=[int(x)for x in input("Enter the price and quantity separated by space: ").split()]
price=inputs[0]
quantity=inputs[1]
gst=0.18
total_price=price*quantity
total_gst=(total_price*gst)
total_amount=total_price+total_gst
print("Total price: ", total_price)
print("GST: ", total_gst)
print("Final bill:", total_amount)