tries=0
while tries<3:
    pin=int(input("Enter your pin: "))
    if pin==1234:
        print("Access granted")
        break
    else:
        print("Incorrect pin.")
        tries+=1
else:
    print("Card blocked.")